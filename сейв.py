import pickle
game_data = {
'позиция-игрока' : 'С23 В45',
'карманы' : ['ключи', 'карманный нож', 'гладкий камень'],
'рюкзак' : ['веревка', 'молоток', 'яблоко'],
'деньги' : 158.50
}
save_file = open('save.dat', 'wb')
pickle.dump(game_data, save_file)
save_file.close()
