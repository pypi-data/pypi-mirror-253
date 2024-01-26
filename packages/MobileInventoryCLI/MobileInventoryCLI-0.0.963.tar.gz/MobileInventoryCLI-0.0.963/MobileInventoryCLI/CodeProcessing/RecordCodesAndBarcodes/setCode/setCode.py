from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.DB.db import *
from datetime import datetime


class SetCode:
	def setCodeFromBarcode(self):
		print("SetCode")
		if self.engine != None:
			with Session(self.engine) as session:
				while True:
					try:
						barcode=input("barcode: ")
						#checks needed here
						query=session.query(Entry).filter(Entry.Barcode==barcode)
						results=query.all()
						if len(results) < 1:
							print("No Results")
						else:
							r=None
							if len(results) == 1:
								r=results[0]
							elif len(results) > 1:
								try:
									while True:
										for num,i in enumerate(results):
											print(f"{num} -> {i}")
										select=input("which Entry: ")
										select=int(select)
										r=results[select]
										break
								except Exception as e:
									print(e)
							if r != None:
								ncode=input("New Code: ")
								r.Code=ncode
								session.commit()
								session.flush()
								session.refresh(r)
								print(r)



						break
					except Exception as e:
						print(e)

	def __init__(self,engine=None):
		self.engine=engine
		cmds={
		'setCode from Barcode':{
								'cmds':['cfb','1','code<bc'],
								'exec':self.setCodeFromBarcode,
								'desc':"set Code from Barcode"
			},
		'quit':{
				'cmds':["q","quit","2"],
				'exec':lambda self=self:exit("user quit!"),
				'desc':"quit progam"
				},
		'back':{

				'cmds':['b','back','3'],
				'exec':None,
				'desc':"go back a menu if any"
				}
		}

		while True:
			for cmd in cmds:
				print(f"{cmds[cmd]['cmds']} - {cmds[cmd]['desc']}")
			action=input("Do What? : ")
			for cmd in cmds:
				try:
					if action.lower() in cmds[cmd]['cmds'] and cmds[cmd]['exec']!=None:
						cmds[cmd]['exec']()
						break
					elif action.lower() in cmds[cmd]['cmds'] and cmds[cmd]['exec']==None:
						return
					else:
						raise Exception(f"Invalid Command! {action}")
				except Exception as e:
					print(e)

if __name__ == "__main__":
	SetCode()