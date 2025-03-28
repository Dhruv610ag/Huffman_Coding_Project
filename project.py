import heapq   
import os

class BinaryTreeNode:
    def __init__(self,value,frequency) -> None:
        self.value=value
        self.frequency=frequency
        self.left=None
        self.right=None
    
    def __lt__(self,other)-> bool:
        return self.frequency<other.frequency
    
    def __eq__(self, __value: object) -> bool:
        return self.frequency==__value.frequency
 
class HuffmanCoding:
    def __init__(self,path) -> None:
        self.path=path
        self.__heap=[]
        self.__codes={}
        self.__reverse_codes={}
        
    def __make_frequency_dict(self,text):
        freq_dict={}
        for char in text:
            if char not in freq_dict:
                freq_dict[char]=0
            freq_dict[char]+=1
        return freq_dict
    
    def __buildheap(self,freq_dict):
        for key in freq_dict:
            frequency=freq_dict[key]
            binary_tree_node=BinaryTreeNode(key,frequency)
            heapq.heappush(self.__heap,binary_tree_node)
            
    def __buildTRee(self):
        while(len(self.__heap)>1):
            binary_tree_node_1=heapq.heappop(self.__heap)
            binary_tree_node_2=heapq.heappop(self.__heap)
            freq_sum=binary_tree_node_1.frequency + binary_tree_node_2.frequency
            newNode=BinaryTreeNode(None,freq_sum)
            newNode.left=binary_tree_node_1
            newNode.right=binary_tree_node_2
            heapq.heappush(self.__heap,newNode)
        return
    
    def __buildcodehelper(self,root,curr_bits):
        if root is None:
            return 
        if root.value is not None:
            self.__codes[root.value]=curr_bits
            self.__reverse_codes[curr_bits]=root.value
            return 
        self.__buildcodehelper(root.left,curr_bits+"0")
        self.__buildcodehelper(root.right,curr_bits+"1")
        
    def __buildcodes(self):
        root=heapq.heappop(self.__heap)
        self.__buildcodehelper(root,"")
        return 
    
    def __getEncodedText(self,text):
        encoded_text= ""
        for char in text:
            encoded_text+=self.__codes[char]
        return encoded_text
    
    def __getPaddedEncodedText(self,encoded_text):
        padded_amount = 8 - (len(encoded_text) % 8)
        for i in range(padded_amount):
            encoded_text+='0'
        padded_info="{0:08b}".format(padded_amount) 
        padded_encoded_text=padded_info+encoded_text
        return padded_encoded_text
        
    def __getBytesArray(self,padded_encoded_text):
        array=[]
        for i in range(0,len(padded_encoded_text),8):
            byte=padded_encoded_text[i:i+8]
            array.append(int(byte,2))
        return array
    
    def compression(self):
        #get file from the path
        #read text from the file
        file_name,file_extension=os.path.splitext(self.path)
        output_path=file_name + ".bin"
        with open(self.path,'r+') as file,open(output_path,'wb') as output:
            text=file.read()
            text=text.rstrip()
            # make frequency dictionary using the text
            freq_dict=self.__make_frequency_dict(text)
            #construct the heap from the frequency dict
            self.__buildheap(freq_dict)
            #construct the binary tree from the heap
            self.__buildTRee()
            #genearte the codes from the binary tree
            self.__buildcodes()
            #creating the encoded text using the cides
            encoded_text=self.__getEncodedText(text)
            #put this encoded text into the binary file
            
            #pad  this encoded text
            padded_encoded_text=self.__getPaddedEncodedText(encoded_text)
            bytes_array=self.__getBytesArray(padded_encoded_text)
            #return this binary file as the output
            final_bytes=bytes(bytes_array)
            output.write(final_bytes)
        print("Compressed Completed .You can have a look at it ")
        return output_path
    
    def __removePadding(self,text):
        padded_info=text[:8]
        extra_padding=int(padded_info,2)
        text=text[8:]
        text_after_padding_removed=text[:-1*extra_padding]
        return text_after_padding_removed
    
    def __decodeText(self,text):
        decoded_text=""
        current_bits=""
        for bit in text:
            current_bits+=bit
            if current_bits in self.__reverse_codes:
                character=self.__reverse_codes[current_bits]
                decoded_text+=character
                current_bits=""
        return decoded_text
                
        
    def decompress(self,input_path):
        file_name,file_extension=os.path.splitext(self.path)
        output_path=file_name + "_decompress" +".txt"
        with open(input_path,'rb') as file,open(output_path,'w') as output:
            bit_string=""
            byte=file.read(1)
            while byte:
                byte=int.from_bytes(byte, 'big')
                bits=bin(byte)[2:].rjust(8, '0')
                bit_string+=bits
                byte=file.read(1)
            actual_text=self.__removePadding(bit_string)
            decompressed_text=self.__decodeText(actual_text)
            output.write(decompressed_text)
        print("Decompression completed .You can have a look at it")
        return output_path    
            
path="/Users/dhruv/Desktop/hufffman Coding Project/sample.txt"  
h=HuffmanCoding(path)
output_path=h.compression()  
h.decompress(output_path)
    
    
        