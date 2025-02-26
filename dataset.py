import csv

# List of example encryption and decryption commands
encrypt_commands = [
    "Encrypt the file located at /media/downloads/document.pdf",
    "Secure the file at /home/user/images/photo.jpg",
    "Apply encryption to the file in /backups/files/image.png",
    "Protect the file /data/private/video.mp4",
    "Lock the file at /user/documents/report.docx",
    "Run encryption on the file /media/secure/audio.mp3",
    "Please encrypt the file in /archives/2023/file.zip",
    "Ensure encryption for /backup/critical/info.txt",
    "Encrypt this document: /downloads/docs/contract.pdf",
    "Start encryption for /shared/important/photo.jpg",
    "Encrypt the file located at /documents/personal/data.csv",
    "Apply secure encryption to /media/files/project.pptx",
    "Please lock /downloads/secure/file.mp4",
    "Add encryption to /user/photos/private/photo123.jpg",
    "Start the encryption process on /backup/archive.zip",
    "Encrypt and protect the file located at /temp/folder/file.docx",
    "Run encryption on /data/videos/movie.avi",
    "Secure the contents of /backup/family/photos.jpeg",
    "Encrypt this file: /mydocs/private/diary.txt",
    "Start encryption for /system/logs/backup.log",
    "Apply strong encryption to /user/files/confidential.pdf",
    "Encrypt and secure /media/private/database.sql",
    "Please encrypt /backup/old/files/photo2020.jpg",
    "Add encryption to /documents/work/contract.doc",
    "Encrypt /shared/projects/proposal.docx",
    "Protect the file at /media/storage/report.xlsx",
    "Encrypt the contents of /home/user/documents/resume.docx",
    "Lock the file located at /pictures/2022/vacation.jpg",
    "Ensure encryption for /backup/documents/secrets.txt",
    "Apply encryption on /private/data/securefile.zip",
    "Start secure encryption on /user/photos/private/image.png",
    "Encrypt the file at /temp/archive/encrypted.pdf",
    "Protect the file located at /user/docs/confidential.docx",
    "Run encryption on /media/storage/protected-file.mp3",
    "Add strong encryption to /secure/folder/backup.zip",
    "Apply encryption on the file /archive/2023/record.xlsx",
    "Encrypt this folder: /private/photos/family_album/",
    "Encrypt file /documents/secure/notes.txt",
    "Lock and encrypt the folder /backup/old_projects/",
    "Start encryption on /user/files/protected-report.pdf",
    "Encrypt the document located at /shared/private/legal.pdf",
    "Secure the video file at /media/movies/collection/film.mp4"
]


decrypt_commands = [
    "Decrypt the file in /downloads/file.txt using key abc123",
    "Unlock the file at /secure/docs/report.pdf with key 456xyz",
    "Please decrypt the file located at /archive/encrypted.zip with key qwerty123",
    "Open the file at /media/locked/data.docx with decryption key abc@789",
    "Decrypt the document /user/secured/notes.txt with the passcode safe123",
    "Run decryption on /private/folder/image.png using key 123unlock",
    "Release the file /backup/2023/logs.txt with key access456",
    "Decrypt the file in /downloads/archive.doc with key key789",
    "Unlock this folder /home/user/locked/file.pdf with key mykey001",
    "Please open /private/photos/secret.jpg using decryption key mypass999",
    "Decrypt the file located at /mydocs/secure/info.pdf using key zxc456",
    "Unlock and open /documents/encrypted/files/report.docx with key passkey123",
    "Please decrypt the image at /images/locked/image01.jpg with code key001",
    "Run decryption for /backup/encrypted/music.mp3 using key safeunlock",
    "Decrypt the secured folder /data/archive.zip with the passcode pass123",
    "Open the file in /user/secure/videos/clip.mp4 with key unlockkey",
    "Remove encryption from /files/protected/contract.doc with key 123abc",
    "Decrypt and open the file /archive/safe/data.csv using the key 789xyz",
    "Unlock this document /docs/secret.txt with key open123",
    "Start decryption on /home/user/backup/encrypted-video.mp4 using key decryption456",
    "Please decrypt /secure/2023/documents/salary.pdf with key safe456",
    "Open the encrypted file /media/backup/notes.doc with the key unlockme",
    "Decrypt /backup/locked-folder/image01.png with the key passkey2021",
    "Unlock the secure file /data/protected/info.txt with key 789open",
    "Decrypt /files/private/locked-doc.pdf using key decrypt2022",
    "Release and open /archive/private/video.mp4 with key 123unlock",
    "Decrypt the data file /backup/archive/secret.txt using passphrase safe@001",
    "Run decryption for /media/secured/movies/video.avi with key keyunlock",
    "Unlock /user/files/protected/summary.doc with key securekey789",
    "Decrypt this file /temp/locked/document.pdf with key openme123",
    "Please remove encryption on /photos/protected/photo01.jpg with key unlockit",
    "Decrypt the archive /backup/encrypted/files.zip with key 456def",
    "Unlock the report at /data/restricted/info2022.txt using key access2022",
    "Open the encrypted folder /user/docs/sensitive.docx with key decryption123",
    "Decrypt the file /media/personal/video_locked.mp4 with passcode 789xyz",
    "Unlock the file /archive/locked_files/important.doc using key safeopen",
    "Decrypt the file at /documents/encrypted/backup.doc with the key accesscode",
    "Start decryption for /media/restricted/music.mp3 using key unlockpass",
    "Please decrypt the protected file /backup/private/doc2021.pdf with key 987key",
    "Open the encrypted PDF /files/secure/report2023.pdf with key safeaccess",
    "Decrypt the compressed file /downloads/encrypted_archive.zip with key key234"
]



# Open a CSV file and write the data
with open("command_dataset.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Label", "Prompt"])  # Header row
    
    # Write all encrypt commands
    for command in encrypt_commands:
        writer.writerow(["encrypt", command])
        
    # Write all decrypt commands
    for command in decrypt_commands:
        writer.writerow(["decrypt", command])

print("Dataset saved as 'command_dataset.csv'")
