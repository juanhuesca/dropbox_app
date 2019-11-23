import dropbox
import sys
import xlwt

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("sheet1") #creamos una nueva hoja de Excel

dbx = dropbox.Dropbox('Iwolw2b6xQAAAAAAAAAAFApmoXjsHOxUXtQt9-dmXoyUTE-Zm1GLZkiY5nzpScpx')

dbx.users_get_current_account()

filename = "outputfile_23112019.xls"#output nombre de este archivo para Excel

book.save(filename)
i=0

for entry in dbx.files_list_folder("/test1/").entries:#entramos a la carpeta 

	entry.name.encode("utf-8")
	print(entry.name)
	sheet1.write(i,0,entry.name)

	f_link = dbx.sharing_create_shared_link(entry.path_display)#create folder link

	p = f_link.path #get folder path 
	print(p)
	sheet1.write(i,1,p)

	u = f_link.url#get folder url
	print(u)
	sheet1.write(i,2,u)

	i += 1

book.save(filename)
