names=list()
print(f'変更前のlistのidentity:{id(names)}')
names.append('松田')
print(f'変更後のlistのidentity:{id(names)}')

name='松田'
print(f'変更前のstrのidentity:{id(name)}')
name='スーパー'+name
print(f'変更後のstrのidentity:{id(name)}')

name2='松田'
print(f'name2のidentity:{id(name2)}')
