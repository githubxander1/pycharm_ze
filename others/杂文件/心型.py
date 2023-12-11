sentences='i love you dfgfdg gfdgfs hgfhgf fggsddfsg ret erwter gerwtrsg fdsgfd sgdfsg dfsg fdsgdf sg fdg sdf gdfg df sgdf sgdfs gdf sg dfs g df gdf sg df sg df sgdfsg dfsg dfs g dfs gdf sg f dsg fd sg dfs g eg df sg er wt re f er e wt ert er t ertw re wt rewt er yw rewt erw t rewt re wtr ew ew r efd v df bvc x bfd sg tr h tr ygr ewg er fgd gsfd g her y erw g drsg fds g dfs hs '
m,n,count=0.05,0.1,0
for y in range(12,-12,-1):
    row_sentences=''
    for x in range(-30,30):
        function = ((x*m)**2+(y*n)**2-1)**3-(x*m)**2*(y*n)**3
        if function <= 0:
            row_sentences+=sentences[(count)%len(sentences)]
            count +=1
        else:
            row_sentences+=' '
    print(row_sentences)
# 保存到文本
f=open('word.txt', "a+")
f.write("\033[4;31;43m row_sentences+'\n'\033[0m")
f.close()