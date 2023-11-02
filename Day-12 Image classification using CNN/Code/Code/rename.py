import os
os.chdir('D:\AI\Day-12 Image classification using CNN\Code\Code\simple_images\elon_musk')
i=1
for file in os.listdir():
    src=file
    dst="elon"+"_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1

