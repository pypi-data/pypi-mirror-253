def TypeText(Type:str = None,text:str = None,link:str = None,guid:str = None):
	if Type == "MentionText":
		if guid and text != None:
			if guid.startswith('u0'):typeMention = "User"
			return [{"type":"MentionText","mention_text_object_guid":guid,"from_index":0,"length":len(text),"mention_text_object_type":typeMention}]
	elif Type != 'MentionText' and Type != 'hyperlink':
		return [{"from_index": 0, "length": len(text), "type": Type}]
	elif Type == 'hyperlink':
		return [{"from_index":0,"length":len(text),"link":{"hyperlink_data":{"url":link},"type":"hyperlink"},"type":"Link"}]