import argparse

parser = argparse.ArgumentParser(description='Process an encoded string.')
parser.add_argument('-e', '--encoded', type=str, required=True, help='The encoded string to process')

args = parser.parse_args()
encoded_str = args.encoded

# Mapping dictionary
mapping = {  
'ECB4':'1','B4A1':'2','F539':'3','53D1':'4','894E':'5',  
'E155':'6','F446':'7','C48C':'8','8797':'9','BD8F':'0',  
'C9F9':'A','60CA':'B','E1B0':'C','FE36':'D','E759':'E',  
'E9FA':'F','39CE':'G','B434':'H','5E53':'I','4198':'J',  
'8B90':'K','7666':'L','D08F':'M','97C0':'N','D869':'O',  
'7357':'P','E24A':'Q','6888':'R','4AC3':'S','BE3D':'T',  
'8AC5':'U','6FE0':'V','6069':'W','9AD0':'X','D8E1':'Y',
'C9C4':'Z',  
'F641':'a','6C6A':'b','D9BD':'c','418D':'d','B740':'e',  
'E1D0':'f','3CD9':'g','956B':'h','C875':'i','696C':'j',  
'906B':'k','3F7E':'l','4D7B':'m','EB60':'n','8998':'o',  
'7196':'p','B657':'q','CA79':'r','9083':'s','E03B':'t',  
'AAFE':'u','F787':'v','C165':'w','A935':'x','B734':'y',
'E4BC':'z',
'B398':'!','78A7':'@','D9A8':'$','30F6':'%','F7DF':'^',
'F79A':'*','D474':'(','4BEE':')','3B76':'-','ECEC':'_',
'A638':'=','7359':'+','6CF7':'[','6889':'{','C98C':']',
'B352':'}','A1F8':'\\','6248':'|','D8F2':';','D885':':',
'44C4':',','DB5F':'<','3E84':'.','F8C7':'>','76D0':'/',
'57E5':'?'} 

# Split the encoded string into chunks of 4 characters
chunks = [encoded_str[i:i+4] for i in range(0, len(encoded_str), 4)]

# Decode each chunk using the mapping dictionary
decoded_str = ''.join([mapping.get(chunk, '?') for chunk in chunks])  # Use '?' for missing mappings

print(decoded_str)
