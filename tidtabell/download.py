import requests

pdfs = [
"tag_10000-11999.pdf",
"tag_1000-1999.pdf",
"tag_12000-14999.pdf",
"tag_15000-17999.pdf",
"tag_18000-19999.pdf",
"tag_1-999.pdf",
"tag_20000-39999.pdf",
"tag_2000-2999.pdf",
"tag_3000-3999.pdf",
"tag_40000-41999.pdf",
"tag_4000-6999.pdf",
"tag_42000-46999.pdf",
"tag_47000-49999.pdf",
"tag_50000_59999.pdf",
"tag_60000_69999.pdf",
"tag_60000-69999.pdf",
"tag_70000_79999.pdf",
"tag_70000-79999.pdf",
"tag_7000-7999.pdf",
"tag_80000-89999.pdf",
"tag_8000-8999.pdf",
"tag_90000-99999.pdf",
"tag_9000-9999.pdf"
]

for nummer in pdfs :
    data = requests.get("https://www.trafikverket.se/contentassets/dcc15e8edd394f2da97ad00fb6d806d0/"+nummer)
    open(nummer, 'wb').write(data.content)

