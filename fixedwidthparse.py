"""
    Usage: python fixedwidthparse.py <source file> <output file> <spec file> [delimiter]
"""
import sys
import json

class Text_csv: 
    
    def __init__(self,input_file,output_file,specs,seperator=','):
        self.f_input = input_file
        self.f_output = output_file
        self.spec = specs
        self.seperator=seperator
        
    def parse_to_csv(self):
        
        #parse spec json (No need to re-invent this wheel right?)
        with open(self.spec) as jstream:
            spec = json.load(jstream)
            spec['Offsets']=list(map(int,spec['Offsets']))
        
        #Overwrite existing file with header or an empty char
        with open(self.f_output,'w',encoding=spec['FixedWidthEncoding']) as f_out:
            if (spec['IncludeHeader']=='True'):
                head=self.seperator.join(spec["ColumnNames"])
                f_out.write(head)
                f_out.write('\n')
            else:
                f_out.write('')

        #Read the whole file, convert, write in one go
        with open(self.f_input,'r',encoding=spec['FixedWidthEncoding']) as file:
            lines = file.read().splitlines()
            
            newlines=[]

            #Insert delimiter to each line and save to newlines[]
            for line in lines:
                newlines += [self.seperator.join(\
                [line[sum(spec['Offsets'][:i]):sum(spec['Offsets'][:i+1])] \
                for i in range(0,len(spec['Offsets']))])]

            #Append to the output file 
            with open(self.f_output,'a',encoding=spec['FixedWidthEncoding']) as f_out:
                f_out.write('\n'.join(newlines))  

if __name__=='__main__':
    text_csv_ = Text_csv(sys.argv[1],sys.argv[2],sys.argv[3],',')
    text_csv_.parse_to_csv()




