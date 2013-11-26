import libtcodpy

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

def handle_keys():
    global playerx, playery
        
    key = libtcodpy.console_wait_for_keypress(True)
        
    if key.vk == libtcodpy.KEY_ENTER and key.lalt:
        libtcodpy.console_set_fullscreen(not libtcodpy.console_is_fullscreen())
            
    elif key.vk == libtcodpy.KEY_ESCAPE:
        return True
    
    if libtcodpy.console_is_key_pressed(libtcodpy.KEY_UP):
        playery = playery - 1
            
    elif libtcodpy.console_is_key_pressed(libtcodpy.KEY_DOWN):
        playery = playery + 1
            
    elif libtcodpy.console_is_key_pressed(libtcodpy.KEY_LEFT):
        playerx = playerx - 1
            
    elif libtcodpy.console_is_key_pressed(libtcodpy.KEY_RIGHT):
        playerx = playerx + 1 

libtcodpy.console_set_custom_font('arial10x10.png', libtcodpy.FONT_TYPE_GREYSCALE | libtcodpy.FONT_LAYOUT_TCOD)
libtcodpy.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)
libtcodpy.sys_set_fps(LIMIT_FPS)

playerx = SCREEN_WIDTH/2
playery = SCREEN_HEIGHT/2

while not libtcodpy.console_is_window_closed():
    libtcodpy.console_set_default_foreground(0, libtcodpy.white)
    libtcodpy.console_put_char(0, playerx, playery, '@', libtcodpy.BKGND_NONE)
    libtcodpy.console_flush()
    libtcodpy.console_put_char(0, playerx, playery, ' ', libtcodpy.BKGND_NONE)
    
    exit = handle_keys()
    
    if exit:
        break
    
    