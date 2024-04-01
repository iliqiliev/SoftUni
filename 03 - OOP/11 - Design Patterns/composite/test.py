from composite import File, Directory

# Create root directory
root = Directory("Root")

# Create subdirectories
documents = Directory("Documents")
music = Directory("Music")
pictures = Directory("Pictures")

# Add subdirectories to root
root.add_entry(documents)
root.add_entry(music)
root.add_entry(pictures)

# Create files in Documents
resume = File("Resume.docx")
report = File("Annual_Report.pdf")
documents.add_entry(resume)
documents.add_entry(report)

# Create files in Music
song1 = File("Favorite_Song.mp3")
song2 = File("Another_Great_Song.mp3")
music.add_entry(song1)
music.add_entry(song2)

# Create files in Pictures
image1 = File("Vacation_Photo.jpg")
image2 = File("Profile_Picture.png")
pictures.add_entry(image1)
pictures.add_entry(image2)

# Create a subdirectory in Documents
old_documents = Directory("Old")
documents.add_entry(old_documents)

# Create files in Old Documents
old_resume = File("Old_Resume.docx")
old_report = File("Old_Annual_Report.pdf")
old_documents.add_entry(old_resume)
old_documents.add_entry(old_report)

# Thanks, AI
print(root.structure())
