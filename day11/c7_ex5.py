orgName,cpName=input('コピー元のファイルパスとコピー後のファイルパスを入力＞＞').split(',')
with open(orgName,'r',encoding='utf-8') as reader,open(cpName,'w',encoding='utf-8') as writer:
    for line in reader:
        writer.write(line)
