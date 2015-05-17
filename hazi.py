# -*- coding: utf-8 -*-

def scramble(inputString):
	if (inputString==''):
		return('String cannot be empty!')
		
	utfString=inputString.decode('utf8')  #decoding UTF-8
	splitString=utfString.split()
	final=''
	wordCount=len(splitString)
	currWordNo=0
	
	for word in splitString: 
		currWordNo+=1
		charCount=len(word)
		
		if(charCount>3):
			unorderedList=list(word)
			fstchar=unorderedList[0]
			punctNo=''
			isPunct=0
			punctList=[":",".","!","?",",",";"]
			for punctMark in punctList:
				if (punctMark in unorderedList[charCount-1]): #is there a punctuation mark after the word?
					punctNo=unorderedList[charCount-1]
					del unorderedList[charCount-1]
					charCount-=1
					isPunct=1
			
			lstchar=unorderedList[charCount-1]
			del unorderedList[0]
			del unorderedList[charCount-2]
			orderedList=(list(reversed(unorderedList)))
			orderedList.append(lstchar)
			orderedList.insert(0,fstchar)
			
			if(isPunct==1):
				orderedList.append(punctNo)
				
			orderedWord=''.join(orderedList)
			if (currWordNo==wordCount):
				final+=(orderedWord)    #if it is the last word, no space is needed
			else:
				final+=(orderedWord+' ')
		else:
			if (currWordNo==wordCount):
				final+=(word)           #if it is the last word, no space is needed
			else:						
				final+=(word+' ')
	return(final)
	
	
	
	



	

