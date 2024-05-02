import os
import eyed3



directory = os.listdir(f"C:/Users/{os.getlogin()}/Music")
lenghs = {}
for item in directory:
    lenghs[len(item)]=item
spaces = max(lenghs)+20
for i in directory:
    data = eyed3.load(f"C:/Users/{os.getlogin()}/Music/{i}")
    
    title_name = data.tag.title
    
        
    artist_name = data.tag.artist
    