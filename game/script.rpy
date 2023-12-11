# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Książe",color="#4b6369")
define f = Character("Księżna",color="#99252f")

init:
    $ flash = Fade(.10, 0, .75, color="#fff")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.



    #Czesc 1



    scene sala_drzwi with fade
    pause 1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy
    play sound "audio/drzwi_zamkniecie.mp3"
    pause 1



    image krol_portret_R = "krol_portret.png"
    image krol_portret_L = im.Flip("krol_portret.png", horizontal="True")
    image krolowa_portret_R = "krolowa_portret.png"
    image krolowa_portret_L = im.Flip("krolowa_portret.png", horizontal="True")

    show krol_portret_L at left with easeinleft
    show krolowa_portret_R at right with easeinright

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."
    f "Tę ucztę wszyscy będą długo pamiętać."
    f "Była wyjątkowo... udana."
    m "Muszę przyznać, że pomysł miałaś idealny."
    m "Oby tylko służba należycie wysprzątała tę salę."
    f "Jutro nie zobaczysz już ani śladu."
    f "Należy nam się odpoczynek. Marzę już tylko o naszym łożu."
    f "Będziesz mi towarzyszyć?"
    m "Jeszcze nie. Moja głowa potrzebuje trochę innego odpoczynku. Spacer dobrze mi zrobi."
    f "Wiesz gdzie mnie znaleźć."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    hide krolowa_portret_R with easeoutright

    m "{i}Czas się przejść.{/i}"

    hide krol_portret_L with easeoutleft

    scene korytarz with fade

    show krol_portret_R at center with easeinright

    m "{i}Może cała ta uczta to nie był dobry pomysł{/i}"
    m "{i}I ta klątwa... co jeśli jednak istnieje?{/i}"

    play sound "audio/szelest.mp3"
    pause 1.5

    window hide

    scene hall_3d with fade
    hide krol_portret_R

    window show
    m "{i}Hmm?{/i}"
    m "{b}Kto tam jest?!{/b}"
    m "{b}Pokaż się!{/b}"
    window hide

    pause 1
    scene hall_3d_oczy with dissolve
    pause 1

    window show
    play sound "audio/krzyk1.mp3"
    m "{b}AAAAAA!!!{/b}"
    window hide

    play sound "audio/bieganie.mp3"

    image wiezaL = "wieza_pietro.png"
    image wiezaR = im.Flip("wieza_pietro.png", horizontal="True")
    image schodyL = "wieza_schody.png"
    image schodyR = im.Flip("wieza_schody.png", horizontal="True")

    scene korytarz with fade
    pause 1
    scene wiezaL with fade
    pause 1
    scene schodyL with fade
    pause 1
    play sound "audio/bieganie.mp3"
    scene wiezaR with fade
    pause 1
    scene schodyR with fade
    pause 1
    scene wiezaL with fade
    pause 1
    scene schodyL with fade
    pause 1
    play sound "audio/upadek.mp3"
    pause 1.5
    scene black with flash
    pause 5
    stop sound


    #Czesc 2



    scene sypialnia with dissolve
    pause 1
    show krol_portret_R at right with dissolve


    window show

    m "Moja głowa... Au."

    play music "audio/ambient1.mp3" volume 0.5

    show krolowa_portret_L at left with easeinleft
    f "Oh, nareszcie! Nawet nie wiesz jak się o ciebie martwiłam najdroższy!"

    $ syp_1 = False
    $ syp_2 = False
    $ syp_3 = False


label sypialnia_dialog:

    menu:
        "Gdzie ja jestem?":
            f "W naszej sypialni. Ale nie podnoś się tak szybko- potrzebujesz odpoczynku."
            $ syp_1 = True
        "Która godzina?":
            f "Słońce wysoko, już niemal południe."
            $ syp_2 = True
        "Co się stało?":
            f "Ty lepiej odpowiedz. Nie było cię całą noc, a nad ranem służba znalazła cię nieprzytomnego w wieży!"
            $ syp_3 = True

if syp_1 == False or syp_2 == False or syp_3 == False:
    jump sypialnia_dialog
else:
    jump sypialnia_dalszy_dialog

label sypialnia_dalszy_dialog:

    f "Najważniejsze, że nic ci się nie stało."
    f "Co właściwie robiłeś w środku nocy, w wieży, kompletnie sam?!"

    menu:
        "Coś mnie goniło":
            m "Nic szczególnego. Udałem się na krótki spacer, ale cały czas miałem wrażenie, że ktoś mnie śledzi."
            m "Usłyszałem dziwny hałas. Odwróciłem się, ale nikogo za mną nie było! Tylko pusty, ciemny korytarz. Zawołałem więc: Pokaż się!"
            m "Wtem w cieniu dostrzegłem czerwone ślepia!"
            m "Pobiegłem więc na wieżę."
            m "To ta klątwa! Biada nam!"
            f "Klątwa, klątwa... Nie ma żadnej klątwy!"
            f "Skończ już z tą klątwą!"
            f "Wypiłeś za dużo, to pewnie tylko twoje majaki."
            $ syp_powiedzial = True

        "Tak tylko się przechadzałem":
            f "Ogranicz wino. I samotne spacery w środku nocy."
            $ syp_powiedzial = False

    f "Odpoczywaj. Ja muszę dopilnować, by służba doprowadziła salę do porządku."
    f "Poślę zaraz po ciepły posiłek dla ciebie."

    window hide
    hide krolowa_portret_L with easeoutleft
    pause 1
    scene pozniej with dissolve
    pause 2
    scene sypialnia with dissolve
    show krol_portret_R at center with dissolve
    window show

    m "Ileż można czekać... Szybciej sam pójdę."
    window hide
    hide krol_portret_R with easeoutleft

    scene korytarz with fade
    show krol_portret_R at center with dissolve

    menu:
        "Idź do kuchni":
            hide krol_portret_R with easeoutright
            $ najpierw_kuchnia = True
            jump kuchnia
        "Idź do sali balowej":
            hide krol_portret_R with easeoutleft
            $ najpierw_kuchnia = False
            jump sala_balowa

label kuchnia:

    scene spizarnia_zamknieta with fade
    show krol_portret_L at left with easeinleft
    window show
    m "Hm... Gdzie się wszyscy podziali do licha?"
    m "Chyba nie potrzeba całej służby by przygotować jeden posiłek dla swojego pana..."
    window hide

    play sound "audio/drzwi_otwarcie.mp3"
    pause 0.5
    show spizarnia_otwarta_mysz behind krol_portret_L with dissolve
    show krol_portret_L at left with dissolve
    pause 0.5

    play sound "audio/krzyk2.mp3"
    m "{b}AAAAAA!!!{/b}"
        
    pause 1
    play sound "audio/drzwi_trzasniecie.mp3"

    hide spizarnia_otwarta_mysz with dissolve
    pause 0.5
    m "{b}{i}CO TO BYŁO?! MYSZ?!{/i}{/b}"
    m "{b}{i}To niemożliwe, przecież nie ma tak wielkich myszy!{/i}{/b}"

    window hide
    pause 0.5
    play sound "audio/drzwi_otwarcie_powoli.mp3"
    pause 0.2
    show spizarnia_otwarta behind krol_portret_L with dissolve

    window show
    m "{i}Przed chwilą jeszcze tu była.{/i}"
    m "{i}Może mi się przywidziało.{/i}"
    pause 0.15
    m "{i}Chyba straciłem apetyt... {/i}"

    if najpierw_kuchnia == True:
        m "{i}Lepiej sprawdzę jak idą porządki.{/i}"
        window hide
        pause 0.2
        hide krol_portret_L with easeoutleft
        scene korytarz with dissolve
        show krol_portret_R with easeinright
        hide krol_portret_R with easeoutleft
        jump sala_balowa

    else:
        m "{i}To naprawdę dziwny dzień. Lepiej się położę.{/i}"
        window hide
        pause 0.2
        hide krol_portret_L with easeoutleft
        jump powrot


label sala_balowa:

    scene sala_drzwi with fade
    pause 0.5
    window show

    if syp_powiedzial == True:
        m "{i}Co jeśli wczoraj nic mi się nie przewidziało? Jeśli naprawdę ktoś lub coś mnie śledzi?{/i}"
        m "{i}Sam już nie wiem w co mam wierzyć.{/i}"

    else:
        m "{i}Może powinienem jej powiedzieć o tym co się wczoraj stało?{/i}"
        m "{i}Chociaż pewnie i tak by mi nie uwierzyła.{/i}"

    window hide
    pause 0.2
    play sound "audio/drzwi_otwarcie.mp3"
    scene sala_drzwi_otwarte with dissolve
    pause 1
    play sound "audio/chodzenie.mp3"
    pause 0.5
    scene sala_krew with dissolve
    pause 2
    window show

    m "Co do...?"
    m "{b}Czyja to krew?!{/b}"
    m "{i}Służba! No dalej, ktokolwiek! Służba!{/i}"

    window hide

    play sound "audio/bieganie_krotkie.mp3"
    scene korytarz with dissolve
    pause 0.5
    show krol_portret_L at left with easeinleft
    pause 0.5
    show krolowa_portret_R at right with dissolve

    window show

    f "Gdzie tak pędzisz, coś się stało?"
    m "{b}K... krew! Dużo krwi! W sali...{/b}"
    f "W sali balowej? Niemożliwe, wszystko zostało uprzątnięte. Osobiście tego dopilnowałam."
    m "{b}Chodź! Jak nie wierzysz to ci pokażę!{/b}"

    window hide

    play sound "audio/bieganie_krotkie.mp3"
    hide krol_portret_L at left with easeoutleft
    hide krolowa_portret_R at left with easeoutleft

    pause 0.3
    scene sala with dissolve

    show krol_portret_L at left with easeinleft
    show krolowa_portret_R at right with easeinright

    pause 0.2
    window show
    m "Ale..."
    m "...cała kałuża krwi."
    f "Mówiłam, żebyś ograniczył wino. Chyba naprawdę mocno uderzyłeś się w głowę tej nocy."
    f "Połóż się lepiej zanim znowu służba będzie musiała cię wnosić do twojego własnego łóżka."
    window hide
    hide krolowa_portret_R at right with easeoutright
    pause 0.5
    window show
    m "{i}Mogłem przysiąc, że była tu krew...{/i}"

    if najpierw_kuchnia == True:
        m "{i}To naprawdę dziwny dzień. Lepiej się położę.{/i}"
        window hide
        pause 0.2
        hide krol_portret_L with easeoutleft
        jump powrot

    else:
        m "{i}Ale po drodzę pogonię tę hołotę. Kto to widział zostawić pana głodnego...{/i}"
        window hide
        pause 0.2
        hide krol_portret_L with easeoutleft
        scene korytarz with dissolve
        show krol_portret_L with easeinleft
        hide krol_portret_L with easeoutright
        jump kuchnia


label powrot:

    scene korytarz_krew with dissolve

    if najpierw_kuchnia == True:
        show krol_portret_L at left with easeinleft
    else:
        show krol_portret_R at right with easeinright

    pause 1
    window show
    m "{b}Znowu krew?!{/b}"
    m "{b}Czy to... moja korona?!{/b}"
    m "{i}Zaraz zaraz, przecież mam swoją koronę na głowie.{/i}"
    m "{i}O co w tym wszystkich chodzi?{/i}"
    m "{i}Złe rzeczy się tutaj dzieją...{/i}"
    m "{i}Hmmm...{/i}"
    window hide
    pause 2
    window show
    m "{i}Wiem!{/i}"
    m "{i}Spadając ze schodów musiałem przecież stracić przytomność! To wszystko to tylko zły sen!{/i}"
    m "{i}Wielkie myszy mogą pojawiać się tylko w snach!{/i}"
    m "{i}Tylko jak mam się teraz obudzić?{/i}"
    window hide
    pause 1
    window show
    m "{i}Mogę spróbować wyskoczyć przez okno z sypialni.{/i}"
    m "{i}Taki szok to by i martwego wybudził.{/i}"
    m "{i}Ale skąd mam mieć pewność, że to tylko zły sen...{/i}"
    m "{i}Jeśli jednak to wszystko się dzieje naprawdę, to oznacza tylko jedno - klątwa istnieje!{/i}"
    m "{i}Skoro i tak jestem przeklęty to co za różnica...{/i}"
    m "{i}Muszę spróbować.{/i}"
    window hide

    if najpierw_kuchnia == True:
        hide krol_portret_L with dissolve
    else:
        hide krol_portret_R with dissolve

    pause 0.5

label sypialnia_okno:
    stop music fadeout 5.0
    scene sypialnia_okno with dissolve
    pause 1
    scene sypialnia_okno at Zoom((1280, 720), (0, 0, 1280, 720), (0, 0, 480, 270), 5.0)
    pause 1
    window show
    m "{i}I tak nie mam nic do stracenia.{/i}"
    m "{i}Dobra, wdech...wydech.{/i}"
    window hide

    play sound "audio/skok.mp3"
    play sound "audio/krzyk3.mp3"
    pause 1.5
    scene black with flash
    pause 5
    scene schodyL with fade
    pause 1
    window show
    m "{i}JA ŻYJĘ!{/i}"
    m "{i}CZYLI TO JEDNAK BYŁ...{/i}"
    m "{i}Ała, moja głowa...{/i}"
    m "{i}...{/i}"
    m "{i}Co ja tutaj wogóle robiłem?{/i}"
    m "{i}A, no tak.{/i}"
    m "{i}AAAAAA!!!{/i}"
    window hide

    play sound "audio/bieganie_krotkie.mp3"

    pause 1

    scene gora_wiezy with fade

    pause 1
    window show
    m "{i}Cholera! Dokąd teraz?!{/i}"
    m "{i}Może ucieczka na wieżę nie była najmądrzejszym pomysłem.{/i}"
    window hide
    pause 2
    scene gora_wiezy_oczy with dissolve
    pause 3
    scene gora_wiezy with dissolve
    pause 1
    scene gora_wiezy_myszy with dissolve
    pause 5
    scene black with dissolve
    pause 2
    scene autorzy with dissolve

    pause
    # This ends the game.

    return
