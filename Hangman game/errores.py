def intentos(errores):
    
    if errores == 0:
        return """
                    ||=================
                    ||        
                    ||        O
                    ||        
                    ||        
                    ||
                    =======@==== ======
                    ||               ||        
                    Puedes equivocarte solamente 4 veces"""
    
    elif errores == 1:
        return """
                    ||=================
                    ||        |
                    ||        O
                    ||        
                    ||        
                    ||
                    =======@==== ======
                    ||               ||           
"""
    
    elif errores == 2:
        return """
                    ||=================
                    ||        |
                    ||        O
                    ||        | 
                    ||         
                    ||
                    =======@==== ======
                    ||               ||        
        """
    
    elif errores == 3:
        return """
                    ||=================
                    ||        |
                    ||        O
                    ||       /| 
                    ||         
                    ||
                    =======@==== ======
                    ||               ||        
        """

    elif errores == 4:
        return """
                    ||=================
                    ||        |
                    ||        O
                    ||       /|\ 
                    ||         
                    ||
                    =======@==== ======
                    ||               ||        
        """
    else :
        return """
                    ||=================
                    ||        |
                    ||        O
                    ||       /|\ 
                    ||       /  
                    ||
                    =======@==== ======
                    ||               ||
                    Juego terminado      
        """
