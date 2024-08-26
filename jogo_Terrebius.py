                                                                                         # IMPORT'S
import os
import random
import time
import pygame

                                                                                        ### MUSICA ###

os.system("cls")                                                                         # VARIAVEIS
inimigo = 's'                                            
contagem_senha = []
senhas = []
senhas_x = [] 
senha = random.randint(100000,999999)
senhas.append(f'{senha}')
 

for y, z in enumerate(senhas):
    senhas_x.append(z)

enc = 2
forca = 1.0
coracao = 5
x = 3
bonus = 0.06              
                                                                    ########################## DEF's #############################
def musica ():
    pygame.mixer.init()
    pygame.mixer.music.load("Sealed Vessel (Hollow Knight)  EPIC VERSION.mp3")
    volume = 0.03
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

def musica2 ():
    pygame.mixer.init()
    pygame.mixer.music.load("Hollow Knight OST - Title Theme.mp3")
    volume = 0.17
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

def musica_combate ():
    pygame.mixer.init()
    pygame.mixer.music.load("Akame x Esdeath(little extended).mp3")
    volume = 0.04
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

def stop_musica ():
    pygame.mixer.music.stop()

def musica_carta ():
    pygame.mixer.init()
    pygame.mixer.music.load("(efeito sonoro  do baú do Clash royale).mp3")
    volume = 0.09
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
 
def musica_final_combate ():
    pygame.mixer.init()
    pygame.mixer.music.load("Final Fantasy Victory Fanfare - Sound Effect [HQ].mp3")
    volume = 0.09
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    time.sleep(3.5)
    pygame.mixer.music.stop()

def musica_fundo_final ():
    pygame.mixer.init()
    pygame.mixer.music.load("Skirmish.mp3")
    volume = 0.04
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

def musica_combate_final ():
    pygame.mixer.init()
    pygame.mixer.music.load("Epic Dark Battle Music - Escape [Powerful Fantasy Horror by Ebunny].mp3")
    volume = 0.04
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    
   
def vidaa ():
    
    if vidaf == 100 and vidav == 100:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
            [][][][][][][][][][][][][][][][]                                                                                                                                                  [][][][][][][][][][][][][][][][]
                           
            ''')
    elif vidaf >= 70 and vidaf <= 89 and vidav >= 90:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
            [][][][][][][][][][][][]                                                                                                                                                          [][][][][][][][][][][][][][][][]
                  ''')
    elif vidaf >= 70 and vidaf <= 89 and vidav >= 70 and vidav <= 89:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
            [][][][][][][][][][][][]                                                                                                                                                          [][][][][][][][][][][][]
                           
            ''')
    elif vidaf >= 40 and vidaf <= 69 and vidav >= 70 and vidav <= 89:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
            [][][][][][][][]                                                                                                                                                                  [][][][][][][][][][][][]
                           
            ''')
    elif vidaf >= 70 and vidaf <= 89 and vidav >= 40 and vidav <= 69:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
            [][][][][][][][][][][][]                                                                                                                                                          [][][][][][][][]
                  ''')
    elif vidaf >= 90 and vidaf >=70 and vidav <= 89:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
            [][][][][][][][][][][][][][][][]                                                                                                                                                  [][][][][][][][][][][][]
                  ''') 
    elif vidaf >= 40 and vidaf <=69 and vidav >=40 and vidav <= 69:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
            [][][][][][][][]                                                                                                                                                                  [][][][][][][][]
                  ''') 
    elif vidaf >= 10 and vidaf <= 39 and vidav >=40 and vidav <= 69:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
            [][]                                                                                                                                                                              [][][][][][][][]
                  ''') 
    elif vidaf >= 1 and vidaf <= 39 and vidav >= 1 and vidav <= 39:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
            [][]                                                                                                                                                                              [][]
                  ''') 
    elif vidaf >= 40 and vidaf <=69 and vidav >= 1 and vidav <= 39:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
            [][][][][][][][]                                                                                                                                                                  [][]
                  ''')
    elif vidaf >= 70 and vidaf <=89 and vidav >= 1 and vidav <= 39:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
            [][][][][][][][][][][][]                                                                                                                                                          [][]
                  ''')
    elif vidaf >= 1 and vidaf <=39 and vidav >= 70 and vidav <= 89:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
            [][]                                                                                                                                                                              [][][][][][][][][][][][]
                  ''')
    elif vidaf <= 0  and vidav >= 1 and vidav <= 39:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
                                                                                                                                                                                              [][]
                    ''')
    elif vidaf >= 1 and vidaf <= 39  and vidav <= 0:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
            [][]                                                                                                                                                                                  
                    ''')
    elif vidaf >= 40 and vidaf <=69 and vidav <= 0:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
            [][][][][][][][]                                                                                                                                                                  
                  ''')
    elif vidaf >= 70 and vidaf <=89 and vidav <= 0:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
            [][][][][][][][][][][][]                                                                                                                                                          
                  ''')
    elif vidaf <= 0 and vidav >= 40 and vidav <= 69:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
                                                                                                                                                                                              [][][][][][][][]
                  ''') 
    elif vidaf <= 0 and vidav >= 70 and vidav <= 89:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
                                                                                                                                                                                              [][][][][][][][][][][][]
                           
            ''')
    elif vidaf >= 40 and vidaf <= 69 and vidav >= 90:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
            [][][][][][][][]                                                                                                                                                                  [][][][][][][][][][][][][][][][]
                  ''')
    elif vidaf >= 1 and vidaf <= 39 and vidav >= 70 and vidav <= 89:
            print(f'''
                    {nome_do_personagem}                                                                                                                                                                     {inimigo}                                          
            ________________________________                                                                                                                                                  ________________________________                                                                                                        
            [][]                                                                                                                                                                              [][][][][][][][][][][][]
                           
            ''')        

            

def clear_screen():
    os.system("cls")

def vela ():
    print('''                ,'                                                                                                                                                                                                            ,'
               @                                                                                                                                                                                                             @
              | |                                                                                                                                                                                                           | |
            __| |__                                                                                                                                                                                                       __| |__
          ''')

def corac ():
    
    if coracao == 5:
        text = (f''' 
                                                                                                  ##   ##    ##   ##    ##   ##    ##   ##    ##   ##  
                                                                                                 #########  #########  #########  #########  #########
                                                                                                  #######    #######    #######    #######    #######
                                                                                                    ###        ###        ###        ###        ###   ''')   
        print(f"{text}") 
        vela()                                                                                                                                                                                                                        
        print(f'''                                                                                                                    />__________________                                                                                           
                                                                                                            [#####[] ____ {nome_do_personagem}   ___/                                                                           
                                                                                                                    \>                                    ''')
        time.sleep(2.0)
    elif coracao == 4:
       
        text = (''' 
                                                                                                              ##   ##    ##   ##    ##   ##    ##   ##    
                                                                                                             #########  #########  #########  #########  
                                                                                                              #######    #######    #######    #######    
                                                                                                                ###        ###        ###        ###        ''')   
        print(f"{text}")
        vela()
        print(f'''                                                                                                                            />__________________ 
                                                                                                                    [#####[] ____ {nome_do_personagem}   ___/
                                                                                                                            \>                   ''')
        time.sleep(2.0)
    elif coracao == 3:
        text = (''' 
                                                                                                                    ##   ##    ##   ##    ##   ##       
                                                                                                                   #########  #########  #########    
                                                                                                                    #######    #######    #######       
                                                                                                                      ###        ###        ###                

                                                                                    ''')   
        print(f"{text}")
        vela()
        print(f'''                                                                                                                            />__________________ 
                                                                                                                    [#####[] ____ {nome_do_personagem}   ___/
                                                                                                                            \>                   ''')
        time.sleep(2.0)
    elif coracao == 2:
        text = (''' 
                                                                                                                              ##   ##    ##   ##           
                                                                                                                             #########  #########      
                                                                                                                              #######    #######          
                                                                                                                                ###        ###                ''')  
        time.sleep(2.0)
        print(f"{text}")
        vela()
        print(f'''                                                                                                                                />__________________ 
                                                                                                                        [#####[] ____ {nome_do_personagem}   ___/
                                                                                                                                \>                   ''')   
    elif coracao == 1:
        text = (''' 
                                                                                                                                     ##   ##    
                                                                                                                                    #########       
                                                                                                                                     #######             
                                                                                                                                       ###                         ''')  
        time.sleep(2.0) 
        print(f"{text}")
        vela()
        print(f'''                                                                                                                                   />______________________ 
                                                                                                                            [#####[] ____ {nome_do_personagem}   ___/
                                                                                                                                \>                   ''')
        time.sleep(2.0)
def terrebius ():
    print('''
          
          
          
          
          
          
          
          
          
          
                                                    
          
          
          
                                                                                                     
                                                                                        
                                                            MMP""MM""YMM    `7MM"""YMM      `7MM"""Mq.      `7MM"""Mq.      `7MM"""YMM     `7MM"""Yp,     `7MMF'   `7MMF'  `7MF    '.M"""bgd 
                                                            P'   MM   `7     MM     `7       MM   `MM.       MM   `MM.       MM     `7      MM      Yb      MM      MM       M      ,MI     "Y 
                                                                 MM          MM   d          MM   ,M9        MM   ,M9        MM   d         MM     dP       MM      MM       M      `MMb.     
                                                                 MM          MMmmMM          MMmmdM9         MMmmdM9         MMmmMM         MM"""bg.        MM      MM       M       `YMMNq. 
                                                                 MM          MM   Y   ,      MM  YM.         MM  YM.         MM   Y  ,      MM     `Y       MM      MM       M          .`MM 
                                                                 MM          MM      ,M      MM   `Mb.       MM   `Mb.       MM     ,M      MM      ,9      MM      YM.     ,M    Mb       dM 
                                                               .JMML.       .JMMmmmmMMM     JMML. .JMM..    JMML. .JMM..    JMMmmmmMMM     .JMMmmmd9      .JMML.     `bmmmmd"'     P"Ybmmd"  
                                                                                        
                                                                                                           
      
      ''')


   
def game_over():    
    print("""                  
        
                
                                                                                                         _____          ___  ___ ______   ______      ________ _____ 
                                                                                                        / ____|    /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
                                                                                                        | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
                                                                                                        | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
                                                                                                        | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
                                                                                                        \_____/_/     \_\_|  |_|______|  \____/   \/   |______|_|  \_/


                                                                                                                            _..--""---.                                
                                                                                                                            /           ".                              
                                                                                                                            `            l                              
                                                                                                                            |'._  ,._ l/"\                              
                                                                                                                            |  _J<__/.v._/                              
                                                                                                                            \( ,~._,,,,-)                              
                                                                                                                              `-\' \`,,j|                               
                                                                                                                                \_,____J                               
                                                                                                                            .--.__)--(__.--.                            
                                                                                                                            /  `-----..--'. j                            
                                                                                                                            '.- '`--` `--'  \\                            
                                                                                                                            //  '`---'`  `-' \\                           
                                                                                                                           //   '`----'`.-.-' \\                          
                                                                                                                         _//     `--- -'   \' | \________                 
                                                                                                                        |  |         ) (      `.__.---- -'\               
                                                                                                                         \7          \`-(               74\\\             
                                                                                                                         ||       _  /`-(               l|//7__           
                                                                                                                         |l    ('  `-)-/_.--.          f''` -.-"|         
                                                                                                                         |\     l\_  `-'    .'         |     |  |         
                                                                                                                         llJ   _ _)J--._.-('           |     |  l         
                                                                                                                         |||( ( '_)_  .l   ". _    ..__I     |  L         
                                                                                                                         ^\\\||`'   "   '"-. " )''`'---'     L.-'`-.._    
                                                                                                                            \ |           ) /.              ``'`-.._``-.
                                                                                                                            l l          / / |                      |''|
                                                                                                                             " \        / /   "-..__                |  |
                                                                                                                             | |       / /          1       ,- t-...J_.'
                                                                                                                             | |      / /           |       |  |        
                                                                                                                             J  \  /"  (            l       |  |        
                                                                                                                             | ().'`-()/            |       |  |        
                                                                                                                            _.-"_.____/             l       l.-l        
                                                                                                                        _.-"_.+"|                  /        \.  \       
                                                                                                                  /"\.-"_.-"  | |                 /          \   \      
                                                                                                                  \_   "      | |                1            | `'|     
                                                                                                                    |ll       | |                |            i   |     
                                                                                                                    \\\       |-\               \j ..          L,,'. `/ 
                                                                                                                    __\\\     ( .-\           .--'    ``--../..'      '-.
                                                                                                                     `'''`----`\\\\ .....--'''                          
                                                                                                                                \\\\                          
                                                            
                                                            """)
    
def carta():
    print ("""
                                        ##+++++++++++++++++++++++++++++++++++      ++++++++++++++++++++++++###+++####+++++      #######################+++###########++
                                        MM++####@@####mm##@@::##############@      ##++++#####++#############++#+#####++++      ##@#####################++++++#######++
                                        mm######++######mm@@@@MM--@@MM##..@@#      ########m###++++#####7############g#+++      #####################################++
                                        mm####::++##############MM::####MM###      #####################################++      ############             ############mm
                                        mm########################@@::####++#      #########m#######     #7##############+      #########                  ##########mm
                                        ++######mm++MM##@@      ######MM##@@M      #########m##             ##########g###      #########      ######        ########mm
                                        ++###############       ##########@@#      #########m       ##$      #############      #################+####      ###+#####++
                                        ++##############        MM##########m      +########     ########     #####g##@@$#      ###############+++####     ###+++####++
                                        ++##mm@@##@@##          ##########++#      ++#########$########$$#    $@#####g####      ++###+++############      #####+#####++
                                        ++..#########     #     ##########::@      ++#######m###########7#    @####g######      ##++++#########$         ############++
                                        ++@@@@######     ##     ############@      ++###++##m###########7    ######g######      ######++++######3          ############
                                        ++mm###############     #############      ++###++++m##########    ########g######      #######################       #########
                                        ++#################     #############      ++#######m######$$    7##########g#####      ########################      #########
                                        ++#################     #############      ++#######m######     ##7##########g####      #######################       #######++
                                        ++#################     #############      ++#######m####     ###7##########g#####      ######################       ########++
                                        ++##MM#############     ############$      ++#######m#     ####7##########g#######      ##########       ###         ########++
                                        ++@@MM#############     ########@@###      #########                   #####g#####      ##########@@              #@#@#######++
                                        ++##@@#############     #######@@##MM      #########                   ###g#######      ##############          #############++
                                        ++##MM###############################      #########m######################g######      ########+#####################+++++++++
                                        ++##MM######################@@##@@###      #####+++++m###+##################g#####      ######+++####################++########
                                        ++##############@@################MM@      ###++++##m#########7####++++####g######      #####++++###################+++++++####
                                        +##@@##########@@##########@@########      +++++####m#########7######+++###g######      ##############################++++++###
                                        ++MM################################m      #########m#########7########++##g######      ############################+++++++++++
                """)
    escolha = input('Escolha a carta 1 , 2 ou 3 para ganhar um bonus: ')
    clear_screen()
    global forca
    if escolha == '1' or escolha == '2' or escolha == '3':
        lista = [0.05,0.05,0.05, 0.07, 0.07, 0.10, 0, 0, 0]
        sorte = random.choice(lista)
        forca += sorte
        print(f'Voce escolheu a carta de numero [{escolha}] e ganhou {sorte * 100 :.0f}% de força')
        musica_carta()
        time.sleep(2.5)
        stop_musica()
        
    else:
        lista = [0.05,0.05,0.05, 0.07, 0.07, 0.10, 0, 0, 0]
        sorte = random.choice(lista)
        maq = (1, 2, 3)
        maq1 = random.choices(maq, k=1)
        print(f"A maquina escolheu o {maq1} {sorte * 100 :.0f}% de força")
        musica_carta()
        time.sleep(3.0)
        stop_musica()
        forca += sorte


def caveiraA():
                                                                                    print("""                  
                                                                                          
                                                                                          
                                                                                          
                                                                                          


                                                                                          
                                                                                          
                                                                                                                        VOCÊ MORREU!!!
                                                                                                                                        
                                                                                                                      @@@@@@@@@@@@@@@@@@@                   `
                                                                                                                @@@@@@                   @@@@@@@                
                                                                                                            @@@@                              @@@@              
                                                                                                           @@@                                  @@            
                                                                                                        @@                                         @ @           
                                                                                                        @@                     `                    @@          `
                                                                                                       @@                                             @@          
                                                                                                       @@ @@                                       @@ @@          
                                                                                                       @@ @@                                       @@  @          
                                                                                                       @@ @@                                       @@  @          
                                                                                                       @@  @@                                      @@ @@          
                                                                                                        @@  @@                                    @@  @@          
                                                                                                         @@ @@      @@@@@@@@@      @@@@@@@@      @@ @@           
                                                                                                         @@ @@@   @@@@@@@@@@@      @@@@@@@@@@   @@@ @@           
                                                                                                         @@ @@@@  @@@@@@@@@@@      @@@@@@@@@@   @@@             
                                                                                                    @@@@    @@@@   @@@@@@@@@        @@@@@@@@@  @@@       @@@@   
                                                                                                @@@@@    @@   @@     @@@@@@    @@@   @@@@@@@   @@@    @@   @@@@@  
                                                                                               @@         @@   @@@           @@@@@@@         @@@@   @@         @@  
                                                                                                 @@@     @@@@    @@@         @@@@@@@        @@@    @@@@      @@@ 
                                                                                               @@          @@@@@@@@           @@@@@         @@@@@@@@@           @@
                                                                                               @@@@@@@         @@@@@@          @@@       @@@@@@@@         @@@@@@@@
                                                                                                     @@@ @@@@@     @@ @@@             @@@ @@      @@@@@@ @@@ 
                                                                                                          @@@@@@  @@@  @@             @@  @@@   @@@@@@        
                                                                                                               @@@@@@  @@ @@@@@@@@@@@ @@  @@@@@@              
                                                                                                                    @@ @@ @ @ @ @ @ @ @ @ @@                 
                                                                                                                  @@@@@  @ @ @ @ @ @ @ @  @@@@@              
                                                                                                              @@@@@@@ @@   @@@@@@@@@@@@@   @@ @@@@@@@            
                                                                                                    @@@@@@@@@@@@      @@                  @@      @@@@@@@@@    
                                                                                                   @@              @@@@@@@             @@@@@@@            @@   
                                                                                                    @@@       @@@@@      @@@@@@@@@@@@@@@    @@@@@       @@@    
                                                                                                        @@   @@@             @@@@@@@@@         @@@   @@      
                                                                                                        @@  @@                                   @@  @@      
                                                                                                         @@@@                                    @@@@   
                                                                                                    
                                                                                                        
                                                                                                                                                                    """)
 
def caveira():
    clear_screen()   
    caveiraA()    
    print('                                                                                                                         Carregando...')
    time.sleep(0.6)
    clear_screen()
    caveiraA()
    print('                                                                                                                         Carregando..')
    time.sleep(0.6)
    clear_screen()
    caveiraA()
    print('                                                                                                                         Carregando.')
    time.sleep(0.6)
    clear_screen()
    caveiraA()
    print('                                                                                                                         Carregando...')
    time.sleep(0.6)
    clear_screen()
    caveiraA()
    print('                                                                                                                         Carregando..')
    time.sleep(0.6)
    clear_screen()
    caveiraA()
    print('                                                                                                                         Carregando.')
    time.sleep(0.6)
    clear_screen()
    caveiraA()
    print('                                                                                                                         Carregando...')
    time.sleep(0.6)
    clear_screen()
    caveiraA()
    print('                                                                                                                         Carregando..')
    time.sleep(0.6)
    clear_screen()
    caveiraA()
    print('                                                                                                                         Carregando.')
    time.sleep(0.6)
    clear_screen()
    caveiraA()
    print('                                                                                                                         Carregando...')
    time.sleep(0.6)
    clear_screen()
    caveiraA()
    print('                                                                                                                         Carregando..')
    time.sleep(0.6)
    clear_screen()
    caveiraA()
    print('                                                                                                                         Carregando.')
    time.sleep(0.6)
    clear_screen()
    caveiraA()
    print('                                                                                                                         Carregando...')
    clear_screen()

def carregando():
    clear_screen()       
    print('                                                                                                                         Carregando...')
    time.sleep(0.6)
    clear_screen()
    print('                                                                                                                         Carregando..')
    time.sleep(0.6)
    clear_screen()
    print('                                                                                                                         Carregando.')
    time.sleep(0.6)
    clear_screen()
    print('                                                                                                                         Carregando...')
    time.sleep(0.6)
    clear_screen()
    print('                                                                                                                         Carregando..')
    time.sleep(0.6)
    clear_screen()
    print('                                                                                                                         Carregando.')
    time.sleep(0.6)
    clear_screen()
    print('                                                                                                                         Carregando...')
    time.sleep(0.6)
    clear_screen()
    print('                                                                                                                         Carregando..')
    time.sleep(0.6)
    clear_screen()
    print('                                                                                                                         Carregando.')
    time.sleep(0.6)
    clear_screen()
    print('                                                                                                                         Carregando...')
    time.sleep(0.6)
    clear_screen()
    print('                                                                                                                         Carregando..')
    time.sleep(0.6)
    clear_screen()
    print('                                                                                                                         Carregando.')
    time.sleep(0.6)
    clear_screen()
    print('                                                                                                                         Carregando...')
    clear_screen()

def oi():
    for i, p in enumerate(message):
        time.sleep(0.06) 
        print(p ,end= '', flush=True)
    print()
    
def castelo ():
    global message
    print(f'                                                                                          Com {nome_do_personagem} de volta, a paz reina novamente no castelo!                                                              ')
    print('''
                                                                                                                                                      !_        
                                                                                                                                                      |*~=-.,   
                                                                                                                                                      |_,-'`    
                                                                                                                                                      |         
                                                                                                                                                      |         
                                                                                                                                                     /^\        
                                                                                                                        !_                          /   \       
                                                                                                                        |*`~-.,                    /,    \      
                                                                                                                        |.-~^`                    /#"     \     
                                                                                                                        |                       _/##_   _  \_   
                                                                                                                   _   _|  _   _   _           [ ]_[ ]_[ ]_[ ]  
                                                                                                                 [ ]_[ ]_[ ]_[ ]_[ ]            |_=_-=_ - =_|   
                                                                                                                !_ |_=_ =-_-_  = =_|           !_ |=_= -    |    
                                                                                                                |*`--,_- _        |            |*`~-.,= []  |    
                                                                                                                |.-'|=     []     |   !_       |_.-"`_-     |    
                                                                                                                |   |_=- -        |   |*`~-.,  |  |=_-      |    
                                                                                                               /^\  |=_= -        |   |_,-~`  /^\ |_ - =[]  |    
                                                                                                           _  /   \_|_=- _   _   _|  _|  _   /   \|=_-      |    
                                                                                                          [ ]/,    \[ ]_[ ]_[ ]_[ ]_[ ]_[ ]_/,    \[ ]=-    |    
                                                                                                           |/#"     \_=-___=__=__- =-_ -=_ /#"     \| _ []  |    
                                                                                                          _/##_   _  \_-_ =  _____       _/##_   _  \_ -    |\   
                                                                                                         [ ]_[ ]_[ ]_[ ]=_0~{_ _ _}~0   [ ]_[ ]_[ ]_[ ]=-   | \  
                                                                                                         |_=__-_=-_  =_|-=_ |  ,  |     |_=-___-_ =-__|_    |  \ 
                                                                                                         | _- =-     |-_   | ((* |      |= _=       | -    |___|
                                                                                                         |= -_=      |=  _ |  `  |      |_-=_       |=_    |/+\|
                                                                                                         | =_  -     |_ = _ `-.-`       | =_ = =    |=_-   ||+||
                                                                                                         |-_=- _     |=_   =            |=_= -_     |  =   ||+||
                                                                                                         |=_- /+\    | -=               |_=- /+\    |=_    |^^^|
                                                                                                         |=_ |+|+|   |= -  -_,--,_      |_= |+|+|   |  -_  |=  |
                                                                                                         |  -|+|+|   |-_=  / |  | \     |=_ |+|+|   |-=_   |_-/ 
                                                                                                         |=_=|+|+|   | =_= | |  | |     |_- |+|+|   |_ =   |=/  
                                                                                                         | _ ^^^^^   |= -  | |  <&>     |=_=^^^^^   |_=-   |/   
                                                                                                         |=_ =       | =_-_| |  | |     |   =_      | -_   |    
                                                                                                         |_=-_       |=_=  | |  | |     |=_=        |=-    |    
                                                                                                                     
                                                                                                                     
                                                                                                                     
                                                                                                                            ______ _               
                                                                                                                            |  ____(_)              
                                                                                                                            | |__   _ _ __ ___      
                                                                                                                            |  __| | | '_ ` _ \     
                                                                                                                            | |    | | | | | | |  _ 
                                                                                                                            |_|    |_|_| |_| |_| (_)
                                             
                                                                                                                       ''')
    print ('''                                                                                                                Criadores:  
                                                                                                                              Yan Brito   
                                                                                                                              José Filipe Brito
                                                                                                                              Jairo Britto  
                                                                                                                              Fabricio Paiva                    
    ''')
    time.sleep(5.0)
    clear_screen()
    print('''
          
          
          
          
          
          
                                                                                                                                CONTINUE...
          
          
          
          
          
          ''')
    time.sleep(2.5)
                                                                                                                                        # JOGO
                                                                                                                                    # INTRODUÇÃO

print('''
    
    
    
Aperte [F11] para tela cheia.''')
f11 = input('''
            
        
        
            
                                                                                                            Aperte [Enter] para começar.''')
musica()
clear_screen()
terrebius()
nome_do_personagem = input('''                                                                               
            
            
            
            
            
            
                                                                                                            Dê um nome ao personagem: ''')
clear_screen()
stop_musica()
musica2()
message = (f'''
        
        
        
        
        
No reino de TERREBIUS existiam dois irmãos, o primogênito chamado {nome_do_personagem} que reinava com justiça e era muito próspero. Porem, seu irmão caçula Febryanja, que, tomado pela inveja, 
decidiu tramar a morte do seu irmão junto ao terrível feiticeiro Vladius Dameron.
Após uma grande comemoração no reino, Febryanja convence {nome_do_personagem} a subirem até a torre do castelo para lhe dar um presente e quando chegam até a torre
o terrível feiticeiro Vladius Dameron lança-lhe um feitiço que o leva direto para o inferno.
Após algum tempo inconsciente, {nome_do_personagem} se viu de frente com o demonio da morte que lhe faz uma proposta em troca de sua alma.
A morte lhe entregará 5 amuletos da vida para que ele possa trazer a cabeça dos 6 monstros que dominam o Hades.
Após derrotar cada monstro a morte lhe dará uma senha para passar pelo portal da ressurreição e conseguir a sua vida de volta e assim 
se vingar do seu irmão e recuperar o seu reino, mas se ele utilizar todos os 5 amuletos a morte terá a posse de sua alma para sempre.
        
        ''')
oi()
time.sleep(2.5)
stop_musica()
musica2()
carregando()                                                                                                                     
clear_screen()
corac()
                                                                            # Inicio
                                    ######################################################################################

message = (f'{nome_do_personagem}, você chegou no Hades')
for i, p in enumerate(message):
    time.sleep(0.06) 
    print(p ,end= '', flush=True)
print()

message = 'Vamos começar, você precisará derrotar os 6 monstros para conseguir a senha do grande portal.'
oi()
message = 'Você chegou em uma encruzilhada, você pode seguir para esquerda, para direita ou para frente.'
oi()
message = 'Lembre de coletar as 3 senhas do caminho da esquerda e as 3 senhas do caminho da direita.'
oi()
time.sleep(1.4)

while True: 
    clear_screen()
    enc += -1
    if enc <= 0:
        musica2()
        message = 'Você voltou para a encruzilhada.'
        oi()

    print(f'                                                                                                                                           senha:{contagem_senha}')
    
    print(f'                                                                                                                                           força: {(forca *100)-100:.0f}%')

    ir = input('digite [e] para esquerda, [d] para direita ou [f] para frente: ')       ######## COMEÇO ESQUERDA ########
    clear_screen()
    corac()
    print(f'                                                                                                                                           força: {(forca *100)-100:.0f}%')
    if ir == 'e':
        carregando()
        stop_musica()
        corac()
        print(f'                                                                                                                                       força: {(forca *100)-100:.0f}%')
        musica_combate ()
        message = "Você chegou na floresta amaldiçoada e encontrou um goblin com 90 de vida e voce tem 100 de vida"
        oi()
        i = input('Aperte enter para golpear')
        vida = 100
        dano1 = 0
        goblin = 90
        dano1 += random.randint(30,120)
        dano1 = dano1 * forca
        message = (f'voce deu {dano1:.0f} de dano')
        oi()
        if dano1 >= 90:
            stop_musica()
            forca += bonus
            musica_final_combate()
            message = (f'voce matou o goblin com um hit e ganhou um bônus de 6% de dano em todos os golpes')
            oi()
            carta()
            message = (f'Voce conseguiu o 1° numero da senha: {z[0]}')
            oi()
            time.sleep(2.0)
            if (f'1° senha: {z[0]}') not in contagem_senha:
                contagem_senha.append(f'1° senha: {z[0]}')
            
        else:
            goblin = random.randint(20,110)
            vida = vida - goblin
            message = (f"O goblin te deu {goblin} de dano e voce ficou com {vida} de vida")
            oi()
            if goblin >= 100:
                coracao = coracao -1
                message = (f"voce morreu e agora tem {coracao} chances")
                oi()
                stop_musica()
                time.sleep(2.0)
                caveira() 
                clear_screen()                                                                                                                                           
                if coracao == 0: 
                    game_over()
                    time.sleep(6.0)                                                                                                                      
                    break                                                                                                                                                                                    
                continue                                      
            
            else:
                message = (f'voce tem direito a mais um hit')
                oi()
                i = input('Aperte enter para golpear novamente')
                dano1 += random.randint(40,100)
                message = (f'voce deu {dano1:.0f} de dano ')
                oi()
            
                if dano1 >= 90:
                    stop_musica()
                    musica_final_combate()
                    message = (f'voce deu {dano1:.0f} de dano e matou o goblin')
                    oi()
                    carta()
                    message = (f'Voce conseguiu o 1° numero da senha: {z[0]}')
                    oi()
                    time.sleep(2.0)
                    if (f'1° senha: {z[0]}') not in contagem_senha:
                        contagem_senha.append(f'1° senha: {z[0]}')
                else:
                    message = (f"voce deu {dano1:.0f} de dano e nao matou o goblin")
                    oi()
                    time.sleep(1.0)
                    coracao = coracao -1
                    message = (f"voce morreu e agora tem {coracao} chances")
                    oi()
                    stop_musica()
                    time.sleep(2.0)
                    caveira()                                                                                                                                  
                    clear_screen()                                                                                                                                          
                    if coracao == 0: 
                        game_over()
                        time.sleep(5.0)                                                                                                                        
                        break                                                                                                                                                                                    
                    continue
        stop_musica()
        clear_screen()
        corac()
        print(f'                                                                                                                                       senha:{contagem_senha}')

        print(f'                                                                                                                                       força: {(forca *100)-100:.0f}%')
        musica_combate()
        monstro = 'Mula sem cabeça'                                         ######## MONSTRO 2 #########
        vogal = 'a'
        message = (f'Voce encontrou {vogal} {monstro} com 90 de vida e voce tem 100 de vida')
        oi()
        i = input('Aperte enter para golpear')
        vida = 100
        dano2 = 0
        dano2 += random.randint(30,120)
        dano2 = dano2 * forca
        message = (f'Voce deu {dano2 :.0f} de dano')
        oi()
        if dano2 >= 90:
            stop_musica()
            forca += bonus
            musica_final_combate()
            message = (f'Voce matou {vogal} {monstro} com um hit e ganhou um bonus de 6% de dano em todos os golpes')
            oi()
            carta()
            message = (f'Voce conseguiu o 2° numero da senha: {z[1]}')
            oi()
            time.sleep(2.0)
            if (f'2° senha: {z[1]}') not in contagem_senha:
                contagem_senha.append(f'2° senha: {z[1]}')
            
        else:
            dano_m = random.randint(30,110)
            vida = vida - dano_m
            message = (f"{vogal.upper()} {monstro} te deu {dano_m} de dano e voce ficou com {vida} de vida")
            oi()
            if dano_m >= 100:
                coracao = coracao -1
                message = (f"voce morreu e agora tem {coracao} chances")
                oi()
                stop_musica()
                time.sleep(2.0)
                caveira()                                                                                                                                                                              
                clear_screen()
                if coracao == 0:
                    game_over()          
                    time.sleep(6.0)
                    break
                continue
            
            else:
                message = (f'Voce tem direito a mais um hit')
                oi()
                i = input('Aperte enter para golpear novamente')
                dano2 += random.randint(30,70)
                message = (f'Voce deu {dano2:.0f} de dano ')
                oi()
            
                if dano2 >= 90:
                    stop_musica()
                    musica_final_combate()
                    message = (f'Voce deu {dano2:.0f} de dano e matou {vogal} {monstro}')
                    oi()                    
                    carta()
                    message = (f'Voce conseguiu o 2° numero da senha: {z[1]}')
                    oi()
                    time.sleep(2.0)
                    if (f'2° senha: {z[1]}') not in contagem_senha:
                        contagem_senha.append(f'2° senha: {z[1]}')
                else:
                    message = (f"voce deu {dano2:.0F} de dano e nao matou {vogal} {monstro}")
                    oi()
                    coracao = coracao -1
                    message = (f"voce morreu e agora tem {coracao} chances")
                    oi()
                    stop_musica()
                    time.sleep(2.0)
                    caveira()                                                                                                                                         
                    clear_screen()                                                                                                                                           
                    if coracao == 0: 
                        game_over() 
                        time.sleep(5.0)                                                                                                                       
                        break
                    continue 
        stop_musica()
        clear_screen()
        corac()  
        print(f'                                                                                                                                       senha:{contagem_senha}')
        
        print(f'                                                                                                                                       força: {(forca *100)-100:.0f}%')
        musica_combate()
        monstro = 'Dragao'                                                  ######### MONSTRO 3 ##########
        vogal = 'o'
        message = (f'Voce encontrou {vogal} {monstro} com 90 de vida e voce tem 100 de vida')
        oi()
        i = input('Aperte enter para golpear')
        vida = 100
        dano3 = 0
        dano3 += random.randint(35,115)
        dano3 = dano3 * forca
        message = (f'Voce deu {dano3 :.0f} de dano')
        oi()
        if dano3 >= 90:
            forca += 0.5
            stop_musica()
            musica_final_combate()
            message = (f'Voce matou {vogal} {monstro} com um hit e ganhou um bonus de 50% a mais de dano em todos os golpes')
            oi()           
            carta()
            message = (f'Voce conseguiu o 3° numero da senha: {z[2]}')
            oi()
            time.sleep(2.0)
            if (f'3° senha: {z[2]}') not in contagem_senha:
                contagem_senha.append(f'3° senha: {z[2]}')
            message = ('Voce chegou ao fim desse caminho va para o proximo')
            oi()
            continue
        else:
            dano_m = random.randint(35,120)
            vida = vida - dano_m
            message = (f"{vogal.upper()} {monstro} te deu {dano_m} de dano e voce ficou com {vida} de vida")
            oi()
            if dano_m >= 100:
                coracao = coracao -1
                message = (f"voce morreu e agora tem {coracao} chances")
                oi()
                stop_musica()
                time.sleep(2.0)
                caveira()                                                                                                                                                                                
                clear_screen()
                if coracao == 0: 
                        game_over()                                                                                                                        
                        break
                continue    
                
            
            else:
                message = (f'Voce tem direito a mais um hit')
                oi()
                i = input('Aperte enter para golpear novamente')
                dano3 += random.randint(20,55)
                message = (f'Voce deu {dano3:.0f} de dano ')
                oi()
            
                if dano3 >= 90:
                    stop_musica()
                    musica_final_combate()
                    message = (f'Voce deu {dano3:.0f} de dano e matou {vogal} {monstro}')
                    oi()
                    carta()
                    message = (f'Voce conseguiu o 3° numero da senha: {z[2]}')
                    oi()
                    time.sleep(2.0)
                    if (f'3° senha: {z[2]}') not in contagem_senha:
                        contagem_senha.append(f'3° senha: {z[2]}')
                    message = ('Voce chegou ao fim desse caminho va para o proximo')
                    oi()
                    continue
                else:
                    message = (f"Voce deu {dano3:.0f} de dano e nao matou {vogal} {monstro}")
                    oi()
                    time.sleep(2.0)
                    coracao = coracao -1
                    message = (f"voce morreu e agora tem {coracao} chances")
                    oi()
                    stop_musica()
                    caveira()                                                                                                                                
                    clear_screen()                                                                                                                                           
                    if coracao == 0: 
                        game_over()
                        time.sleep(6.0)                                                                                                                       
                        break                                                                                                                                                                                    
                    continue
                                                                                                                                                                            
                
    elif ir == "d":                                                  ########## COMEÇO DIREITA #########
        carregando()
        clear_screen()
        corac()                                                                  # MONSTRO 4
        print(f'                                                                                                                                       senha:{contagem_senha}')
        
        print(f'                                                                                                                                       força: {(forca *100)-100:.0f}%')
        musica_combate()
        monstro = 'Orc'
        vogal = 'o'
        message = (f'Voce encontrou {vogal} {monstro} com 90 de vida e voce tem 100 de vida')
        oi()
        i = input('Aperte enter para golpear')
        vida = 100
        dano4 = 0
        dano_m = 90
        dano4 += random.randint(30,125)
        dano4 = dano4 * forca
        message = (f'Voce deu {dano4:.0f} de dano')
        oi()
        if dano4 >= 90:
            stop_musica()
            musica_final_combate()
            forca += bonus
            message = (f'Voce matou {vogal} {monstro} com um hit e ganhou um bonus de 6% de dano em todos os golpes')
            oi()
            carta()
            message = (f'Voce conseguiu o 4° numero da senha: {z[3]}')
            oi()
            if (f'4° senha: {z[3]}') not in contagem_senha:
                contagem_senha.append(f'4° senha: {z[3]}')
            
        else:
            dano_m = random.randint(40,110)
            vida = vida - dano_m
            message = (f"{vogal.upper()} {monstro} te deu {dano_m} de dano e voce ficou com {vida} de vida")
            oi()
            if dano_m >= 100:
                coracao = coracao -1
                message = (f"voce morreu e agora tem {coracao} chances")
                oi()
                stop_musica()
                time.sleep(2.0)
                caveira()                                                                                                                                                                         
                clear_screen()
                if coracao == 0: 
                    game_over() 
                    time.sleep(5.0)                                                                                                                       
                    break
                
                continue
            
            else:
                message = (f'Voce tem direito a mais um hit')
                oi()
                i = input('Aperte enter para golpear novamente')
                dano4 += random.randint(20,70)
                message = (f'Voce deu {dano4:.0f} de dano ')
                oi()
            
                if dano4 >= 90:
                    stop_musica()
                    musica_final_combate()
                    message = (f'voce deu {dano4:.0f} de dano e matou {vogal} {monstro}')
                    oi()                   
                    carta()
                    message = (f'Voce conseguiu o 4° numero da senha {z[3]}')
                    oi()
                    if (f'4° senha: {z[3]}') not in contagem_senha:
                        contagem_senha.append(f'4° senha: {z[3]}')
                    
                else:
                    message = (f"Voce deu {dano4:.0f} de dano e nao matou {vogal} {monstro}")
                    oi()
                    coracao = coracao -1
                    message = (f"Voce morreu e agora tem {coracao} chances")
                    oi()
                    stop_musica()
                    time.sleep(2.0)
                    caveira()                                                                                                                               
                    clear_screen()                                                                                                                                         
                    if coracao == 0: 
                        game_over()
                        time.sleep(6.0)                                                                                                                       
                        break                                                                                                                                                                                    
                    continue
        clear_screen()
        corac()
        print(f'                                                                                                                                       senha:{contagem_senha}')

        print(f'                                                                                                                                       força: {(forca *100)-100:.0f}%')
        musica_combate()
        monstro = 'Serpente'                                            ######### MONSTRO 5 #########
        vogal = 'a'
        message = (f'Voce encontrou {vogal} {monstro} com 90 de vida e voce tem 100 de vida')
        oi()
        i = input('Aperte enter para golpear')
        vida = 100
        dano5 = 0
        dano_m = 90
        dano5 += random.randint(30,110)
        dano5 = dano5 * forca
        message = (f'Voce deu {dano5:.0f} de dano')
        oi()
        if dano5 >= 90:
            stop_musica()
            musica_final_combate()
            forca += bonus
            message = (f'Voce matou {vogal} {monstro} com um hit e ganhou um bonus de 6% de dano em todos os golpes')
            oi()            
            carta()
            message = (f'Voce conseguiu o 5° numero da senha: {z[4]}')
            oi()
            if (f'5° senha: {z[4]}') not in contagem_senha:
                contagem_senha.append(f'5° senha: {z[4]}')
            
        else:
            dano_m = random.randint(30,110)
            vida = vida - dano_m
            message = (f"{vogal.upper()} {monstro} te deu {dano_m} de dano e voce ficou com {vida} de vida")
            oi()
            if dano_m >= 100:
                coracao = coracao -1
                message = (f"Voce morreu e agora tem {coracao} chances")
                oi()
                stop_musica()
                time.sleep(2.0)
                caveira()                                                                                                                                                                          
                clear_screen()
                if coracao == 0: 
                    game_over()
                    time.sleep(5.0)                                                                                                                        
                    break
                        
                continue
            
            else:
                message = (f'Voce tem direito a mais um hit')
                oi()
                i = input('Aperte enter para golpear novamente')
                dano5 += random.randint(30,70)
                message = (f'Voce deu {dano5:.0f} de dano ')
                oi()
            
                if dano5 >= 90:
                    stop_musica()
                    musica_final_combate()
                    message = (f'Voce deu {dano5:.0f} de dano e matou {vogal} {monstro}')
                    oi()                    
                    carta()
                    corac()
                    message = (f'Voce conseguiu o 5° numero da senha {z[4]}')
                    oi()
                    if (f'5° senha: {z[3]}') not in contagem_senha:
                        contagem_senha.append(f'5° senha: {z[4]}')
                    
                else:
                    message = (f"Voce deu {dano5:.0f} de dano e nao matou {vogal} {monstro}")
                    oi()
                    coracao = coracao -1
                    message = (f"Voce morreu e agora tem {coracao} chances")
                    oi()
                    stop_musica()
                    time.sleep(2.0)
                    caveira()                                                                                                                              
                    clear_screen()                                                                                                                                          
                    if coracao == 0: 
                        game_over()
                        time.sleep(6.0)                                                                                                                       
                        break
                    continue
        clear_screen()
        corac()                                                                                                                                                                                    
        print(f'                                                                                                                                       senha:{contagem_senha}')

        print(f'                                                                                                                                       força: {(forca *100)-100:.0f}%')
        musica_combate()
        monstro = 'Grifo'                                                     ############# MONSTRO 6 ############
        vogal = 'o'
        message = (f'Voce encontrou {vogal} {monstro} com 90 de vida e voce tem 100 de vida')
        oi()
        i = input('Aperte enter para golpear')
        vida = 100
        dano6 = 0
        dano_m = 90
        dano6 += random.randint(30,110)
        dano6 = dano6 * forca
        message = (f'Voce deu {dano6:.0f} de dano')
        oi()
        if dano6 >= 90:
            stop_musica()
            musica_final_combate()
            forca += 0.5
            message = (f'Voce matou {vogal} {monstro} com um hit e ganhou um bonus de 6% de dano em todos os golpes')
            oi()           
            carta()
            message = (f'Voce conseguiu o 6° numero da senha: {z[5]}')
            oi()
            if (f'6° senha: {z[5]}') not in contagem_senha:
                contagem_senha.append(f'6° senha: {z[5]}')
            continue
        else:
            dano_m = random.randint(30,130)
            vida = vida - dano_m
            message = (f"{vogal.upper()} {monstro} te deu {dano_m} de dano e voce ficou com {vida} de vida")
            oi()
            if dano_m >= 100:
                coracao = coracao -1
                message = (f"Voce morreu e agora tem {coracao} chances")
                oi()
                stop_musica()
                time.sleep(2.0)
                caveira()                                                                                                                                                                          
                clear_screen()
                if coracao == 0: 
                    game_over()  
                    time.sleep(5.0)                                                                                                                      
                    break
                        
                continue
            
            else:
                message = (f'Voce tem direito a mais um hit')
                oi()
                i = input('Aperte enter para golpear novamente')
                dano6 += random.randint(20,60)
                message = (f'Voce deu {dano6:.0f} de dano ')
                oi()
            
                if dano6 >= 90:
                    stop_musica()
                    musica_final_combate()
                    message = (f'Voce deu {dano6:.0f} de dano e matou {vogal} {monstro}')
                    oi()                   
                    carta()
                    message = (f'Voce conseguiu o 6° numero da senha {z[5]}')
                    oi()
                    if (f'6° senha: {z[5]}') not in contagem_senha:
                        contagem_senha.append(f'6° senha: {z[5]}')
                    continue
                else:
                    message = (f"Voce deu {dano6:.0f} de dano e nao matou {vogal} {monstro}")
                    oi()
                    coracao = coracao -1
                    message = (f"Voce morreu e agora tem {coracao} chances")
                    oi()
                    stop_musica()
                    time.sleep(2.0)
                    caveira()                                                                                                                               
                    clear_screen ()                                                                                                                                         
                    if coracao == 0: 
                        game_over()
                        time.sleep(6.0)                                                                                                                       
                        break                                                                                                                                                                                    
                    continue     
    elif ir == 'f':                                                         ################# FRENTE ##################
        musica2()
        message = (f'Senhas: {contagem_senha}')
        oi()
        message = 'Você chegou no grande portal'
        oi()
        digite_senha = input('Digite a senha do portal: ')
        if digite_senha in senhas:
            stop_musica()
            message = ('Você abriu o portal!!!')
            oi()
            time.sleep(2.0)
            break
        elif digite_senha not in senhas:
            
            message = 'Senha invalida, encontre a senha!'
            oi()
            clear_screen()
            continue    
    else:                                                                   ############ NEM UM NEM OUTRO ##############
        x = x - 1
        if x <= 0:
            message = 'Não seja burro, confira se está com CAPS ligado ou se está digitando errado, digite [e], [d] ou [f] para seguir (-_-`)'
            oi()
            time.sleep(2.0)
            clear_screen()
            continue  
if digite_senha in senhas:
    clear_screen()
    carregando()
    musica_fundo_final()
    message = 'Você voltou para o Reino de Terrebius'
    oi()
    message = (f'''Após derrotar os guardiões do Hades, a morte levou {nome_do_personagem} de volta para o reino de Terrebius, e
{nome_do_personagem} trouxe consigo o poder que adquiriu em cada guardião...
                ''')
    oi()
    time.sleep(1.4)
    clear_screen()
    message = '- Vladius Dameron: Voce não vai escapar assim tão facil Hahahahahahahaa.'
    oi()
    message = (f'- {nome_do_personagem}: É o que veremos.')
    oi()
    message = 'Vladius Dameron apareceu e você deverá derrota-lo para chegar até o castelo.'
    oi() 
    time.sleep(1.5)
    vidav = 100
    vidaf = 100
    stop_musica()
    inimigo = 'Vladius Dameron'
    while True:                                                                  ######### Vladius Dameron #########
        
        clear_screen()
        vidaa()
        clear_screen()
        vidaa()
        musica_combate_final()
        message = 'Escolha 1, 2 ou 3 para golpear.'
        oi()
        i = (input('1: [Soco da morte],  2: [Tormenta do Hades] , 3: [Furia de Terrebius]: '))
        if i == '1' or i == '2' or i == '3':
            if i == '1':
                golpe = 'Soco da morte'
                pronome = 'seu'
                artigo = 'um'
            
            elif i == '2':
                golpe = 'Tormenta do Hades'
                pronome = 'sua'
                artigo = 'uma'
            
            elif i == '3':
                golpe = 'Furia de Terrebius'
                pronome = 'sua'
                artigo = 'uma'
        else:
            continue
        lista_golpes = [0 , 0 , 10 , 20 , 20 , 20, 30]
        danof = random.choice(lista_golpes)
        if danof == 0:
            message = (f'Vladius bloqueou {pronome} {golpe}!')
            oi()
            danov = random.randint(10,30)
            golpe_v = ['Espectro maldito', 'Feitiço atordoante']
            golpev = random.choice(golpe_v)
            vidaf -= danov
            if vidaf <= 0:
                vidaf = 0
            message = (f'Vladius te acertou um {golpev} e te deu {danov} de dano e te deixou com {vidaf:.0f} de vida.')
            oi()
            time.sleep(3.0)
            if vidaf <= 0:
                clear_screen()
                vidaa()
                message = ('Vladius Dameron te derrotou!')
                oi()
                stop_musica()
                game_over()
                time.sleep(4.0)
                break   
            continue                                            
        danoo = danof * forca
        vidav -= danoo
        if vidav <= 0:
            vidav = 0
        message = (f'Voce deu {artigo} {golpe} e deu {danoo:.0f} de dano e deixou Vladius Dameron com {vidav:.0f} de vida.')
        oi()
        time.sleep(3.0)
        if vidav <= 0:
            clear_screen()
            vidaa()
            musica_final_combate()
            message = ('Voce derrotou Vladius Dameron!')
            oi()
            clear_screen()
            break
        danov = random.randint(10,30)
        golpe_v = ['Espectro maldito', 'Feitiço atordoante']
        golpev = random.choice(golpe_v)
        vidaf -= danov
        if vidaf <= 0:
            vidaf = 0
        message = (f'Vladius te acertou um {golpev} e te deu {danov} de dano e te deixou com {vidaf:.0f} de vida.')
        oi()
        time.sleep(3.0)
        if vidaf <= 0:
            clear_screen()
            vidaa()
            message = ('Vladius Dameron te derrotou!')
            oi()
            stop_musica()
            game_over()
            time.sleep(4.0)
            break
        continue
    if vidav == 0:                                                                ############### FEBRYANJA #################     
        musica_fundo_final()
        message = (f'''Após derrotar Vladius Dameron, {nome_do_personagem} utilizou todos os seus poderes lhe restando apenas uma espada 
em seu punho e a sua vontadade de recuperar Terrebius. 
Febryanja assim que percebeu que Vladius Dameron foi derrotado, começou a se preparar para o futuro combate contra seu irmão.
        ''')
        oi()
        carregando()
        message = 'Você entrou no reino.'
        oi()
        message = '- Febryanja: Não esperava ver você novamente, vou te derrotar de uma vez por todas!'
        oi()
        message = (f'- {nome_do_personagem}: Você pagará por tudo que fez comigo e com o meu reino.')
        oi()
        stop_musica()
        time.sleep(1.4)
        vidaf = 100
        vidav = 100
        while True:
            inimigo = 'Febryanja'
            clear_screen()
            vidaa()
            musica_combate_final()
            message = 'Escolha 1, 2 ou 3 para golpear.'
            oi()
            i = (input('1: [para Soco], 2: [para Chute], 3: [Espada]: '))
            if i == '1' or i == '2' or i == '3':
                if i == '1':
                    golpe = 'Soco'
                    pronome = 'seu'
                    artigo = 'um'
                
                elif i == '2':
                    golpe = 'Chute'
                    pronome = 'seu'
                    artigo = 'um'
                
                elif i == '3':
                    golpe = 'Espada'
                    pronome = 'sua'
                    artigo = 'uma'
                
            else:
                continue
            lista_golpes = [0 , 0 , 10 , 20 , 20 , 20, 30]
            danof = random.choice(lista_golpes)
            if danof == 0:
                message = (f'{inimigo} bloqueou {pronome} {golpe}')
                oi()
                danov = random.randint(10,30)
                golpe_v = ['um Soco', 'um Chute', 'uma Espada']
                golpev = random.choice(golpe_v)
                vidaf -= danov
                if vidaf <= 0:
                    vidaf = 0
                message = (f'{inimigo} te acertou {golpev} e te deu {danov} de dano e te deixou com {vidaf:.0f} de vida')
                oi()
                if vidaf <= 0:
                    clear_screen()
                    vidaa()
                    message = (f'{inimigo} te derrotou')
                    oi()
                    stop_musica()
                    game_over()
                    time.sleep(4.0)
                    break   
                continue
            danoo = danof * forca
            vidav -= danoo
            if vidav <= 0:
                vidav = 0
            message = (f'Voce deu {artigo} {golpe} e deu {danoo:.0f} de dano e deixou {inimigo} com {vidav:.0f} de vida')
            oi()
            if vidav <= 0:
                clear_screen()
                vidaa()
                musica_final_combate()
                message = (f'Voce derrotou {inimigo}')
                oi()               
                message = '- Febryanja: Haaaaaa, não acredito que fui derrotado por você, como ficou tão forte?'
                oi()
                message = (f'''- {nome_do_personagem}: Desde que você e o Vladius Dameron me mandaram para o Hades, tive que enfrentar varios monstros
e com isso fiquei mais forte, e pude retornar para reconquistar o meu reino.''')
                oi()
                message = '- Febryanja: Agora eu entendo como ficou tão forte, mas confesso que não achei que você fosse escapar.'
                oi()
                message = (f'''Após derrotar febryanja e reconsquistar seu reino, {nome_do_personagem} aprisionou seu irmão no mais profundo calabouço do castelo 
por muitos e muitos anos.   ''')
                oi()
                time.sleep(2.5)
                castelo()
                
                break
            danov = random.randint(10,30)
            if danov == 10 or danov == 17 or danov == 22 or danov == 28:
                lista_golpes = [10 , 10 , 10 , 20 , 20 , 20, 30]
                danof = random.choice(lista_golpes)
                danoo = danof * forca
                vidav -= danoo
                if vidav <= 0:
                    vidav = 0
                message = (f'Voce deu {artigo} {golpe} e deu {danoo:.0f} de dano e deixou {inimigo} com {vidav:.0f} de vida')
                oi()
                if vidav <= 0:
                    clear_screen()
                    vidaa()
                    musica_final_combate()
                    message = (f'Voce derrotou {inimigo}')
                    oi()
                    message = '- Febryanja: Haaaaaa, não acredito que fui derrotado por você, como ficou tão forte?'
                    oi()
                    message = (f'''- {nome_do_personagem}: Desde que você e o Vladius Dameron me mandaram para o Hades, tive que enfrentar varios monstros
e com isso fiquei mais forte, e pude retornar para reconquistar o meu reino.''')
                    oi()
                    message = '- Febryanja: Agora eu entendo como ficou tão forte, mas confesso que não achei que você fosse escapar.'
                    oi()
                    message = (f'''Após derrotar febryanja e reconsquistar seu reino, {nome_do_personagem} aprisionou seu irmão no mais profundo calabouço do castelo 
por muitos e muitos anos.   ''')
                    oi()
                    time.sleep(2.5)
                    castelo()
                    break
            golpe_v = ['um Soco', 'um chute', 'uma espada']
            golpev = random.choice(golpe_v)
            vidaf -= danov
            if vidaf <= 0:
                vidaf = 0
            message = (f'{inimigo} te acertou {golpev} e te deu {danov} de dano e te deixou com {vidaf:.0f} de vida')
            oi()
            if vidaf <= 0:
                clear_screen()
                vidaa()
                message = (f'{inimigo} te derrotou')
                oi()
                stop_musica()
                game_over()
                time.sleep(4.0)
                break
            continue


                                                         