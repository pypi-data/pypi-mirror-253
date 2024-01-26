"""

"""
from copy import deepcopy
import gzip
import os
import re
import pandas as pd 
import itertools

class Iterator:

    @staticmethod
    def sort_array(arr):
        '''
        element: characters+numerics
        for example: sort chromosome name
        '''
        arr_len = len(arr)
        for i in range(0, arr_len-1):
            for j in range(1, arr_len):
                a=arr[j-1][3:]
                a_char= re.findall(r"[^0-9]", a)
                b=arr[j][3:]
                b_char= re.findall(r"[^0-9]", b)
                #a is char
                if a_char:
                    if b_char==[] or (b_char and a>b):
                        arr[j], arr[j-1] = arr[j-1], arr[j]
                #a_char==[]
                else:
                    if b_char==[] and int(a)>int(b):
                        arr[j], arr[j-1] = arr[j-1], arr[j]
        return arr
    

    @staticmethod
    def search_series(series:pd.Series, index)->list:
        '''
        Note: index name of series must be unique
        '''
        val = series.get(index)
        if val is not None:
            series[index], series.iloc[-1] = series.iloc[-1], series[index]
            # print('##', series)
            return list(val) if type(val) == pd.Series else [val,] 
        return []

    @staticmethod
    def shape_length(input:list, fill_value):
        '''
        [[1,2],[1,2,4]] -> [[1,2,0],[1,2,4]]
        '''
        max_len = 0
        for i in input:
            this_len = len(list(i))
            if this_len > max_len:
                max_len = this_len
        #append fill_value to the end of the list
        for i in range(len(input)):
            if len(input[i]) < max_len:
                val = [fill_value,]*(max_len - len(input[i]))
                input[i] = list(itertools.chain(input[i], val))

    @staticmethod
    def parse_ncbi_acc(infile)->dict:
        '''
        value: NCBI_protein_accession, index: UniProtKB_protein_accession
        source file: *_gene_refseq_uniprotkb_collab.gz
        '''
        accessions = {}
        # infile = os.path.join(self.dir_source, "gene_refseq_uniprotkb_collab.gz")
        df = pd.read_csv(infile, sep='\t', header=0)
        index_name = 'UniProtKB_protein_accession'
        df['acc_group'] = df[index_name].str[:2]
        for name, sub_df in df.groupby(['acc_group']):
            series = None
            if len(sub_df) > 1:
                series = pd.Series(sub_df.iloc['#NCBI_protein_accession'].squeeze())
                series.index = sub_df[index_name]
            elif len(sub_df) == 1:
                series = pd.Series(sub_df.iat[0,0], index=[sub_df.iat[0,1],])
            if series is not None:
                series.index.name = index_name
                series.name = name
                accessions[name] = series
            print(series.shape, series)
            print('\n\n')
        return accessions