import pafy

video = input("Link Youtube : ")
url = pafy.new(video)
print("Video Title \>")
print(url.title)
print("Video Like \>")
print(url.like)
dn = url.getbest()
dn.download()
print("Succes...")