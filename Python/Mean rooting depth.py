#Get height and width of training images
path="Z:/Poem/Rhizoboxes/Backup_RootPainter/drive_rp_sync/datasets/training_data_PE_rhizoboxes"
files=os.listdir(path)

h=[]
w=[]

for file in files:
        
    #Load image and convert to greyscale
    # L = R * 299/1000 + G * 587/1000 + B * 114/1000
    image = np.array(Image.open(path+"/"+file).convert('L'))
    
    h.append(image.shape[0])
    w.append(image.shape[1])

#Get summary statistics for height (training images)
print("Average height: "+str(round(statistics.mean(h)))+" pixels")
print("Minimum height: "+str(round(min(h)))+" pixels")
print("Maximum height: "+str(round(max(h)))+" pixels")

#Get summary statistics for width (training images)
print("Average width: "+str(round(statistics.mean(w)))+" pixels")
print("Minimum width: "+str(round(min(w)))+" pixels")
print("Maximum width: "+str(round(max(w)))+" pixels")

#Image resolution (pixels/cm)
res=94.8135

#List segmented images in repository
path="Z:/Poem/Rhizoboxes/Backup_RootPainter/drive_rp_sync/projects/PE_rhizotrons_2017_1/results/segmentations"
files=os.listdir(path)

#Create empty array to story mean rooting depth values
mrd=[]

for file in files:
        
    #Load image and convert to greyscale (root pixel is 1, background is 0)
    # L = R * 299/1000 + G * 587/1000 + B * 114/1000
    image = np.array(Image.open(path+"/"+file).convert('L'))
    
    #Replace values>0 by 1. Keep value=0 otherwise.
    image = np.where(image>0, 1, 0)
    
    #Median filtering (denoising, 3x3 kernel)
    image = ndimage.median_filter(image, size=3)
    
    #Sum the number of root pixels in each row (use axis=1 for row sums)
    px = np.sum(image, axis=1)
    
    #Calculate total number of root pixels
    totalpx = np.sum(px)
    
    if (totalpx>0):
        
        #Calculate average rooting depth
        depth=np.array(range(0, len(px), 1))*(-1)/res
    
        mrd.append(np.sum(depth*np.array(px))/totalpx)
        
    else:
        
        mrd.append(0)

#Save results in a csv file (results.csv)
output="Z:/Poem/Rhizoboxes/Backup_RootPainter/drive_rp_sync/projects/PE_rhizotrons_2017_1/results/segmentations"
results=pd.DataFrame(data={'image': files, 'mrd':mrd}).sort_values(by='image')
results.to_csv(output+'/results.csv', index=False)