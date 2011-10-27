#!/usr/bin/env python
	
	Le Python

	str = "Coucou"
	str * 2 va donner CoucouCoucou
	str[1] donne o
	str[1:4] donne ouc
	str[-1] donne u
	str[-2:] donne ou // Donne jusqu'à la fin de la chaîne
	len(str) donne la longueur de la chaîne
	str = """
		Coucou bla
				gsgegs
				geg
				agqqqh	gzge
		"""
	if a < 0 :
		print a
	
	Tant qu'il y a des tabulations, on est dans la condition, pas d'accolades

	b = 2
	c = 4
	b,c = c,b
	b donne 4 et c donne 2

	suite de fibbo:
	a,b = 0,1
	while b < 500:
		print b
		a,b = b, a+b
	
	Pas de files, pas de Piles, pas de Tableau : que des LISTES

	l = ['coucou', 'bla']
	l[0] donne coucou
	l * 2 donne ['coucou', 'bla', 'coucou', 'bla']

	str[2] = a donne une erreur
	ajouter un élément dans la liste
	l[1:1] = ["bien"]
	Pour ne rien faire : pass
	exemple : 
	if a < 0 :
		pass
	elif
		...

	for elem in l:
		print elem
	
		
	def dire_kane(n):
		for i in range(n):
			print "kane"
	
	range(4,100,10) // Début : 4, de 10 en 10 jusqu'à 100

	récupérer une frappe de l'utilisateur en lui demandant quelque-chose
	stru = raw_input("Super prompt de Kane, tape rien :")

	if stru in ["Coucou", "bla","bidule"]
	

python.org/doc
