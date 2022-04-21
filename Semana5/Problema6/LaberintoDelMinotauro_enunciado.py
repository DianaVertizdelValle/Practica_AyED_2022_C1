# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:11:27 2022

HALLA LA SALIDA AL LABERINTO Y RECUERDA EL CAMINO DE VUELTA
-----------------------------------------------------------

Implemente el uso de la estructura de datos adecuada
para almacenar los movimientos realizados para hallar 
la salida al laberinto. Debe poder deshacer los movimientos
con la tecla de retroceso (hasta el punto de inicio).
Si se realizan movimientos opuestos de manera consecutiva,
no deben guardarse en el historial del viajante.

@author: Bruno M. Breggia
"""

import pygame, sys, time

# %% Implementacion de clase Direccion

class Direccion:
    
    brujula = {
        pygame.K_UP    : (( 0, 1), "Arriba ↑"    ),
        pygame.K_DOWN  : (( 0,-1), "Abajo ↓"     ),
        pygame.K_RIGHT : (( 1, 0), "Derecha →"   ),
        pygame.K_LEFT  : ((-1, 0), "← Izquierda" ),
        }
    
    def __init__(self, key_event):
        self.direccion = key_event
        
    def __getitem__(self, index):
        # Sobrecarga del operador de indexado []
        return self.brujula[self.direccion][0][index]
        
    def __neg__(self):
        # sobrecarga del operador menos unario
        if self.direccion == pygame.K_UP:
            return Direccion(pygame.K_DOWN)
        if self.direccion == pygame.K_DOWN:
            return Direccion(pygame.K_UP)
        if self.direccion == pygame.K_RIGHT:
            return Direccion(pygame.K_LEFT)
        if self.direccion == pygame.K_LEFT:
            return Direccion(pygame.K_RIGHT)
    
    def __repr__(self):
        # representacion por consola (string)
        return self.brujula[self.direccion][1]
    
    def __eq__(self, other):
        # sobrecarga de operador de igualdad ==
        return self.direccion == other.direccion


# %% Animacion

pygame.init()

dim = 375 # dimension de la ventana cuadrada
screen = pygame.display.set_mode((dim,dim))
maze = pygame.image.load("images/maze_cuadriculado.png")
redDot = pygame.image.load("images/red_dot.png")
redDot = pygame.transform.scale(redDot, (20, 20))
clock = pygame.time.Clock()

paso = 25  # distancia que se avanza por vez
pos_actual = [0.2*paso, dim-4*paso]
teclas_movimiento = [pygame.K_UP, pygame.K_DOWN, 
                     pygame.K_LEFT, pygame.K_RIGHT]

# Ubico punto rojo sobre laberinto
merged = maze.copy()
merged.blit(redDot, pos_actual)

# %% Manejo de eventos

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: # evento del tipo "tecla presionada"
            if event.key in teclas_movimiento:
                avance = Direccion(event.key)
                print(avance)
            elif event.key == pygame.K_BACKSPACE:
                # La tecla de retroceso debe hacer un 
                # bactracking (recorrido inverso)
                continue
            else:
                continue
            
            # actualizo coordenadas del punto rojo
            pos_actual[0] += avance[0]*paso
            pos_actual[1] -= avance[1]*paso
            
            # actualizo imagen de fondo
            merged = maze.copy()
            merged.blit(redDot, pos_actual)
            screen.blit(merged, (0, 0))
        
        elif event.type == pygame.QUIT:
            # cerrar ventana y salir del programa
            pygame.quit()
            sys.exit()
    
    # actualizara fondo
    screen.blit(merged, (0, 0))
    pygame.display.update()
    clock.tick(15)



