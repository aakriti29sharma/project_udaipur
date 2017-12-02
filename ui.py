from tkinter import *
def motions():
	import Motion_detect
def exits():
	exit(0)
root = Tk()

root.geometry('500x500')
btn1 = Button(root,text='Motion Module',command=motions)
lb1 = Label(root,text='\n')
lb1.pack()
btn1.pack()
btn2 = Button(root,text='Exit Module',command=exits)
btn2.pack()
lb2 = Label(root,text='\n')
lb2.pack()
root.mainloop()





# import requests

# # put your keys in the header
# headers = {
#     "app_id": "2b6b7127",
#     "app_key": "443e0a3a38deb423d56a9517d6897d6c"
# }

# payload = '{"image":"https://github.com/00arpit00/images/blob/master/xxx.jpg"}'

# url = "http://api.kairos.com/detect"

# # make request
# r = requests.post(url, data=payload, headers=headers)
# print r.content

