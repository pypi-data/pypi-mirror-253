import sqlalchemy
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base as dbase
from sqlalchemy.ext.automap import automap_base
from datetime import datetime,timedelta
from colored import Fore,Style,Back
from datetime import datetime,timedelta

filename="codesAndBarcodes.db"
DEVMOD=False
if DEVMOD:
	if Path(filename).exists():
		Path(filename).unlink()
dbfile="sqlite:///"+str(filename)
print(dbfile)
#import sqlite3
#z=sqlite3.connect(filename)
#print(z)
ENGINE=create_engine(dbfile)
BASE=dbase()
#BASE.prepare(autoload_with=ENGINE)

class Entry(BASE):
	__tablename__="Entry"
	Code=Column(String)
	Barcode=Column(String)
	#not found in prompt requested by
	'''
	#name {Entryid}
	#name {Entryid} {new_value}
	
	#price {Entryid}
	#price {Entryid} {new_value}

	#note {Entryid}
	#note {Entryid} {new_value}
	
	#size {Entryid} 
	#size {Entryid} {new_value}
	'''
	Name=Column(String)
	Price=Column(Float)
	Note=Column(String)
	Size=Column(String)
	
	CaseCount=Column(Integer)

	Shelf=Column(Integer)
	BackRoom=Column(Integer)
	Display_1=Column(Integer)
	Display_2=Column(Integer)
	Display_3=Column(Integer)
	Display_4=Column(Integer)
	Display_5=Column(Integer)
	Display_6=Column(Integer)
	InList=Column(Boolean)
	Stock_Total=Column(Integer)
	Location=Column(String)
	ListQty=Column(Float)
	upce2upca=Column(String)

	EntryId=Column(Integer,primary_key=True)
	Timestamp=Column(Float)
	def __init__(self,Barcode,Code,upce2upca='',Name='',InList=False,Price=0.0,Note='',Size='',CaseCount=0,Shelf=0,BackRoom=0,Display_1=0,Display_2=0,Display_3=0,Display_4=0,Display_5=0,Display_6=0,Stock_Total=0,Timestamp=datetime.now().timestamp(),EntryId=None,Location='///',ListQty=0.0):
		if EntryId:
			self.EntryId=EntryId
		self.Barcode=Barcode
		self.Code=Code
		self.Name=Name
		self.Price=Price
		self.Note=Note
		self.Size=Size
		self.Shelf=Shelf
		self.CaseCount=CaseCount
		self.BackRoom=BackRoom
		self.Display_1=Display_1
		self.Display_2=Display_2
		self.Display_3=Display_3
		self.Display_4=Display_4
		self.Display_5=Display_5
		self.Display_6=Display_6
		self.Stock_Total=Stock_Total
		self.Location=Location
		self.Timestamp=Timestamp
		self.InList=InList
		self.ListQty=ListQty
		self.upce2upca=upce2upca

	def __repr__(self):
		return f"""{Style.bold}{Style.underline}{Fore.pale_green_1b}Entry{Style.reset}(
		{Fore.hot_pink_2}{Style.bold}{Style.underline}EntryId{Style.reset}={self.EntryId}
		{Fore.violet}{Style.underline}Code{Style.reset}='{self.Code}',
		{Fore.orange_3}{Style.bold}Barcode{Style.reset}='{self.Barcode}',
		{Fore.orange_3}{Style.underline}UPCE from UPCA[if any]{Style.reset}='{self.upce2upca}',
		{Fore.green}{Style.bold}Price{Style.reset}=${self.Price},
		{Fore.red}Name{Style.reset}='{self.Name}',
		{Fore.tan}Note{Style.reset}='{self.Note}',
		{Fore.pale_green_1b}Timestamp{Style.reset}='{datetime.fromtimestamp(self.Timestamp).strftime('%D@%H:%M:%S')}',
		{Fore.deep_pink_3b}Shelf{Style.reset}={self.Shelf},
		{Fore.light_steel_blue}BackRoom{Style.reset}={self.BackRoom},
		{Fore.cyan}Display_1{Style.reset}={self.Display_1},
		{Fore.cyan}Display_2{Style.reset}={self.Display_2},
		{Fore.cyan}Display_3{Style.reset}={self.Display_3},
		{Fore.cyan}Display_4{Style.reset}={self.Display_4},
		{Fore.cyan}Display_5{Style.reset}={self.Display_5},
		{Fore.cyan}Display_6{Style.reset}={self.Display_6},
		{Fore.light_salmon_3a}Stock_Total{Style.reset}={self.Stock_Total},
		{Fore.magenta_3c}InList{Style.reset}={self.InList}
		{Fore.yellow}ListQty{Style.reset}={self.ListQty}
		{Fore.misty_rose_3}Location{Style.reset}={self.Location}
		{Fore.sky_blue_2}CaseCount{Style.reset}={self.CaseCount}
		{Fore.sky_blue_2}Size{Style.reset}={self.Size}
		)
		"""
Entry.metadata.create_all(ENGINE)

tables={
	'Entry':Entry
}

class DayLog(BASE):
	__tablename__="DayLog"
	DayLogId=Column(Integer,primary_key=True)
	EntryId=Column(Integer)
	ScannedCode=Column(String)
	Qty=Column(Float)
	ListNote=Column(String)
	ListName=Column(String)
	date=Column(Date)

	def __init__(self,EntryId,ScannedCode,date,Qty=1,ListName=f'Entry for {datetime.now().month}/{datetime.now().day}/{datetime.now().year}',ListNote=f'Entry for {datetime.now().ctime()}',DayLogId=None):
		self.ScannedCode=ScannedCode
		self.Qty=Qty
		if date:
			self.date=date
		else:
			self.date=datetime.now()

		self.ListName=ListName
		self.ListNote=ListNote
		self.EntryId=EntryId
		if DayLogId:
			self.DayLogId=DayLogId

	def addQty(self,amount):
		self.Qty+=amount
	def minusQty(self,amount):
		self.Qty-=amount
	def clearQty():
		self.Qty=0
	def setQty(self,qty):
		self.Qty=qty

	def __repr__(self):
		return f"""{Fore.cyan}{Style.bold}DayLog{Style.reset}(
	{Fore.red}DayLogId={self.DayLogId}{Style.reset},
	{Fore.green}ScannedCode={self.ScannedCode},{Style.reset}
	{Fore.yellow}EntryId={self.EntryId},{Style.reset},
	{Fore.magenta}Qty={self.Qty},{Style.reset}
	{Fore.GREY_50}ListName={self.ListName},{Style.reset}
	{Fore.tan}ListNote={self.ListNote},{Style.reset}
	{Fore.violet}date={self.date},{Style.reset}
	)"""
DayLog.metadata.create_all(ENGINE)