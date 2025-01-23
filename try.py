from datetime import datetime

src = '09-09-2025'
d = datetime.strptime(src, '%d-%m-%Y')
dst = d.strftime('%Y-%m-%d')
print(dst)