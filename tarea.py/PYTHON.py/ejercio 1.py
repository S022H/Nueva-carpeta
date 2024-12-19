min_otros_cursos=2.5
max_otros_cursos=7
promedio_otros_cursos=4.0
nuetro_curso=1.5

#diferencia de duracion
crudo_promedio=5.0
crudo_dalto=3.5

mini_diferencia = 100-(nuetro_curso/min_otros_cursos * 100)
max_otros_cursos = 100-(nuetro_curso  *1000 // max_otros_cursos / 10)
promedio_otros_cursos = 100-(nuetro_curso / promedio_otros_cursos * 100)


#calculo de duracion de tiempo perdido
tiempo_vacio_promedio= 100 - promedio_otros_cursos * 1000 // crudo_promedio / 10
tiempo_vacio_dalto= 100 - nuetro_curso * 1000 // crudo_dalto / 10

print("-------------------------------------------------------") 
print(f'el curso de dalto dura {mini_diferencia}% menos que el mas rapido')
print(f'el curso de dalto dura {max_otros_cursos}% menos que el mas lento')
print(f'el curso de dalto dura {promedio_otros_cursos}% menos que el promedio')
#tiempo no perdido
print("------------------------------------------------------")
print(f'el curso pierde este tiempo {tiempo_vacio_promedio}%')
print(tiempo_vacio_dalto)
 #equivalente
print("-------------------------------------------------------") 
print(f'ver 10 hora equivale a ver {promedio_otros_cursos * 100 // nuetro_curso / 10} hora de este curso')
print(f'ver 10 hora equivale a ver {nuetro_curso* 100 // promedio_otros_cursos / 10} hora de este curso')
print("-------------------------------------------------------") 
