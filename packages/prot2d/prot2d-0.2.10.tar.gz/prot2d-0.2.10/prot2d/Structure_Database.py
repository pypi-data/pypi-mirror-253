import numpy as np
import subprocess
import pandas as pd
import shutil
import os
import importlib.resources as pkg_resources


#SCOP_summary = '/Users/constantincarl/Uni/BachelorThesis/prot2D/database/SCOP_SF_summary.txt'
class Structure_Database:
    # the obj is created using at least foldseek_executable path and tmp_Dir from the user.
    # db information and data is saved in the package structure itself (default relative paths)
    # --> the data base can be acce
    def __init__(self,foldseek_executable,tmp_dir):
        self.foldseek_executable = foldseek_executable
        self.tmp_dir = tmp_dir
        self.package_data_dir_path = 'PROT2D.SF_database'
        self.SCOP_SF_db_info_tsv = self.load_package_file(self.package_data_dir_path,'db_info.tsv') #SCOP SF info tsv
        self.foldseek_SCOP_db= self.load_package_file(self.package_data_dir_path+'.foldseek_db','db') #SCOP SF database dir
    def load_package_file(self,package_data_dir,filename):
        with pkg_resources.path(package_data_dir,filename) as path:
            return path

    def get_matching_SF_U_T_fixed_region(self,input_pdb, min_prob=0.2):
        try:
            filename = input_pdb.split('/')[-1]  # Gets the filename with extension
            filename_without_ext = '.'.join(filename.split('.')[:-1])
            result_file = self.tmp_dir+'/'+filename_without_ext+'_foldseek_result'

            command = [self.foldseek_executable,'easy-search', input_pdb,self.foldseek_SCOP_db,result_file , self.tmp_dir,'--format-output', 'query,target,qstart,qend,tstart,tend,tseq,prob,alntmscore,u,t,lddtfull,qaln,taln']
            print("run command: "+ str(command))
            subprocess.run(command)
            print("done")

            column_names = ['query', 'target', 'qstart', 'qend', 'tstart', 'tend', 'tseq', 'prob', 'alntmscore', 'u', 't','lddtfull','qaln','taln']
            df = pd.read_csv(result_file, sep='\t', names=column_names)
            max_prob_row = df.loc[df['prob'].idxmax()]
            if max_prob_row['prob']< min_prob:
                print("no matching SF found")
                return None,None,None,None,None
            best_SF_representative = max_prob_row['target'].replace('.pdb','')
            u = max_prob_row['u']
            t = max_prob_row['t']
            q_start = max_prob_row['qstart']
            q_end = max_prob_row['qend']
            t_start = max_prob_row['tstart']
            t_end = max_prob_row['tend']
            lddtfull= max_prob_row['lddtfull'].split(',')
            
            print("qaln:")
            qaln=max_prob_row['qaln']
            print(qaln)
            print("taln:")
            taln= max_prob_row['taln']
            print(max_prob_row['taln'])
            print(taln.count('-'))

            new_lddtfull = []
            lddt_index = 0
            print(len(qaln.replace('-','')))
            print(len(taln.replace('-','')))
            print(len(lddtfull))
            for q_char, t_char in zip(qaln, taln):
                if t_char == '-':
                    # additional residue in input protein
                    new_lddtfull.append(0)
                elif q_char != '-' and t_char != '-':
                    # alignment residue with existing lddt
                    new_lddtfull.append(lddtfull[lddt_index])
                    lddt_index += 1

            ## read in SCOP_db summary file ##
            df = pd.read_csv(self.SCOP_SF_db_info_tsv, sep='\t')
            df.replace({'None': None, 'nan': None}, inplace=True)

            specific_row = df.loc[df['representative'] == best_SF_representative]
            if not df['representative'].eq(best_SF_representative).any():
                print("db error !!!!! (representative in db not in summary file)")
                return None,None,None,None,None,None
            SF = specific_row['SF'].iloc[0]
            fixed_rot_matrix_string = specific_row['rotation_matrix'].iloc[0]
            
            fixed_rot =string_matrix_to_numpy(fixed_rot_matrix_string)
            u_matrix = np.array([float(num) for num in u.split(',')]).reshape(3, 3)
            t_vector = np.array([float(num) for num in t.split(',')])
            print("\n#################")
            print("--- Rotating by inital SF FoldSeek alignment + fixed family rotation ---")
            print(f"input: {filename_without_ext}")
            print(f"SF: {SF} (prob: {max_prob_row['prob']})")
            print(f"representative: {best_SF_representative}")
            print("#################\n")
            
            print(f't_aligned_region ({t_start},{t_end})')
            return SF,u_matrix,t_vector,fixed_rot,(q_start,q_end),new_lddtfull
        except Exception as e:
            print(e)
            return None,None,None,None,None,None

    def initial_and_fixed_Sf_rot_region(self,input_pdb):
        sf,u,t,fixed_rot,aligned_region,lddtfull = self.get_matching_SF_U_T_fixed_region(input_pdb)
        if sf == None:
            destination_file = os.path.join("temp/failed", os.path.basename(input_pdb))
            shutil.copy(input_pdb, destination_file)
            return input_pdb
        U_inv,T_inv = invert_UT(u,t)

        filename = input_pdb.split('/')[-1]  # Gets the filename with extension
        filename_without_ext = '.'.join(filename.split('.')[:-1])
        sf_aligned_rot_pdb = self.tmp_dir+'/'+filename_without_ext+f'_sf-{sf}_aligned_rot.pdb'
        sf_fixed_rot_pdb = self.tmp_dir+'/'+filename_without_ext+f'_sf-{sf}_fixed_rot.pdb'
        empty_t = np.array([0,0,0])
        transform_pdb(input_pdb,sf_aligned_rot_pdb,U_inv,T_inv)
        transform_pdb(sf_aligned_rot_pdb,sf_fixed_rot_pdb,fixed_rot,empty_t)
        return sf_fixed_rot_pdb,aligned_region,lddtfull

    def init_db_from_summary_file(SCOP_summary_file,db_outfile):
        init_matrix= np.array([
        [1,0,0],
        [0,1,0],    
        [0,0,1]
        ])
        summary = pd.read_csv(SCOP_summary_file, sep='\t', na_values=['None', 'nan'])
        summary['rotation_matrix'] = [numpy_matrix_to_string(init_matrix)] * len(summary)
        summary['rotation_type'] = ['automatic'] * len(summary)

        summary.to_csv(db_outfile, sep='\t', index=False)

    def set_manual_SF_rotation(self,SF_number, numpy_rotatoin_matrix, manual=True):
        if not isinstance(numpy_rotatoin_matrix, np.ndarray) or numpy_rotatoin_matrix.shape != (3, 3):
            print("ERROR: Wrong rotation matrix format (numpy 3x3 needed)!")
            print('example:')
            print( np.array([
        [1,0,0],
        [0,1,0],    
        [0,0,1]
        ]))
            return False
        
        db  = pd.read_csv(self.SCOP_SF_db_info_tsv, sep='\t')

        if SF_number not in db['SF'].values:
            print(f"{SF_number} is not a valid SCOP SF number")
            return False
        
        db.loc[db['SF'] == SF_number, 'rotation_matrix'] = numpy_matrix_to_string(numpy_rotatoin_matrix)
        if manual:
            db.loc[db['SF'] == SF_number, 'rotation_type'] = 'manual'
        db.to_csv(self.SCOP_SF_db_info_tsv, sep='\t', index=False)
        print(f"Successfully changed fixed rotation for SF: {SF_number} to {numpy_rotatoin_matrix}")
        return True
    
    def get_SF_info(self,sf_number:int):
        """
        user can input a SCOP SF and get information on the representative etc
        """
        db  = pd.read_csv(self.SCOP_SF_db_info_tsv, sep='\t')
        if sf_number not in db['SF'].values:
                print(f"{sf_number} is not a valid SCOP SF number")
                return False
        else:
            filtered_row = db.loc[db['SF'] == sf_number]
            print(filtered_row)
            return filtered_row
    
def transform_pymol_out_to_UT(get_view_output):
    pymol_matrix_string = get_view_output.replace("(", "").replace(")", "")
    pymol_number_list = [float(num) for num in pymol_matrix_string.split(",")]

    rotation_matrix = np.array(pymol_number_list[:9]).reshape((3, 3), order='F')
    translation_vector = np.array([0, 0, 0]) # no linear object shifting
    return rotation_matrix,translation_vector

def string_matrix_to_numpy(matrix_string):
        number_strings = matrix_string.strip("()").split(",")
        number_floats = [float(num) for num in number_strings]
        matrix = np.array(number_floats).reshape(3, 3)
        return matrix

def numpy_matrix_to_string(matrix):
    matrix_string = ', '.join(map(str, matrix.flatten()))
    return '('+matrix_string+')'

def transform_pdb(pdb_file, output_file, U,T):

    with open(pdb_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as out:
        for line in lines:
            if line.startswith(('ATOM', 'HETATM')):
                # Umwandeln der Koordinaten in Fließkommazahlen
                x = float(line[30:38])
                y = float(line[38:46])
                z = float(line[46:54])

                # Transformation anwenden
                x_new, y_new, z_new = U @ (np.array([x, y, z]) + T)

                # Zeile mit neuen Koordinaten schreiben
                out.write(f"{line[:30]:<30}{x_new:8.3f}{y_new:8.3f}{z_new:8.3f}{line[54:]}")
            else:
                out.write(line)

def invert_UT (U,T):
    U_inv = np.transpose(U)
    T_inv = -T
    return U_inv,T_inv
#rot = transform_pymol_out_to_UT("")
#set_manual_SF_rotation(3000545, rot[0])


