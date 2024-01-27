import aiohttp
import asyncio
import httpx
from arsein.Encoder import encoderjson
from arsein.GtM import default_api
from json import dumps, loads,JSONDecodeError
from random import choice,choices,randint
from arsein.Clien import clien
from arsein.Device import DeviceTelephone
import base64 
from base64 import b64decode
from arsein.Error import ErrorPrivatyKey,ErrorServer,AuthError
from arsein.ErrorRubika import ErrorRubika


async def http(plat:str = None,js:dict = None,OrginalAuth:str = None,auth:str = None,key:str = None,api_version:str = "6"):
	Full = default_api().defaultapi()
	enc,Enc = encoderjson(auth,key),encoderjson(OrginalAuth,key)
	if plat == 'web':
		return httpx.post(Full, data = dumps({"api_version":api_version if api_version != "6" else api_version,"auth": OrginalAuth,"data_enc":enc.encrypt(dumps(js)),"sign": enc.makeSignFromData(enc.encrypt(dumps(js)))}),headers = {"Origin": "https://web.rubika.ir","Referer": f"https://web.rubika.ir/","Host":Full.replace("https://","").replace("/",""),"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"}).text

	elif plat == 'android':
		return httpx.post(Full, data = dumps({"api_version":api_version if api_version != "6" else api_version,"auth": auth,"data_enc":Enc.encrypt(dumps(js)),"sign": Enc.makeSignFromData(Enc.encrypt(dumps(js)))})).text

async def httpfiles(serversfile:str,dade,head:dict):
	return httpx.post(serversfile, data = dade  , headers = head).text


async def httplogin(auths,js:dict):
	Full = default_api().defaultapi()
	enc,Enc = encoderjson(auth = auths),encoderjson(auth = auths)
	return httpx.post(Full, data = dumps({"api_version":"6","tmp_session":auths,"data_enc":enc.encrypt(dumps(js))})).text


class method_Rubika:
	def __init__(self,plat:str = None,OrginalAuth:str = None,auth:str = None,keyAccount:str = None):
		self.Plat = plat
		self.Auth = auth
		self.OrginalAuth = OrginalAuth
		self.keyAccount = keyAccount
		if not keyAccount == None:self.enc = encoderjson(self.Auth , self.keyAccount) if plat == 'web' else encoderjson(self.OrginalAuth , self.keyAccount)

	def methodsRubika(self,types:str = None,methode:str = None,indata:dict = None,wn:dict = None,server = None,podata = None,header:dict = None):
		self.Type = types
		self.inData = {"method":methode,"input":indata,"client":wn}
		self.serverfile = str(server)
		self.datafile = podata
		self.headerfile = header

		while 1:
			try:
				loop = asyncio.get_event_loop()
				# loop.run_until_complete
				for senddata in range(1):
					if self.Type == "json":
						sendJS:dict =  loads(self.enc.decrypt(loads(loop.run_until_complete(http(plat = self.Plat,js = self.inData,OrginalAuth = self.OrginalAuth,auth = self.Auth,key = self.keyAccount))).get("data_enc")))
						if sendJS.get("status") != 'OK':
							stat = ErrorRubika(sendJS).Error
							if stat == "re":
								return ErrorRubika(sendJS).state
							elif stat == "ra":
								ErrorRubika(sendJS)
						else:
							return sendJS
					elif self.Type == "file":
						sendFILE = loop.run_until_complete(httpfiles(serversfile = self.serverfile,dade = self.datafile,head = self.headerfile))
						return sendFILE
					elif self.Type == "login":
						authrnd = encoderjson.changeAuthType(''.join(choices('abcdefghijklmnopqrstuvwxyz',k = 32)))
						self.enc = encoderjson(auth = authrnd)
						sendLOGIN:dict = loads(self.enc.decrypt(loads(loop.run_until_complete(httplogin(auths = authrnd,js = self.inData))).get("data_enc")))
						if sendLOGIN.get("status") != 'OK':
							stat = ErrorRubika(sendLOGIN).Error
							if stat == "re":
								return ErrorRubika(sendLOGIN).state
							elif stat == "ra":
								ErrorRubika(sendLOGIN)
						else:
							return sendLOGIN
					elif self.Type == "service":
						sendSERVICE:dict = loads(self.enc.decrypt(loads(loop.run_until_complete(http(plat = self.Plat,js = self.inData,OrginalAuth = self.OrginalAuth,auth = self.Auth,key = self.keyAccount,api_version = "6"))).get("data_enc")))
						if sendSERVICE.get("status") != 'OK':
							stat = ErrorRubika(sendSERVICE).Error
							if stat == "re":
								return ErrorRubika(sendSERVICE).state
							elif stat == "ra":
								ErrorRubika(sendSERVICE)
						else:
							return sendSERVICE
				break
			except JSONDecodeError:
				continue
			except aiohttp.client_exceptions.ClientConnectorError:
				continue
			except httpx.ConnectError:
				continue
			except aiohttp.client_exceptions.InvalidURL:
				continue