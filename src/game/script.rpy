# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
style say_dialogue:
    outlines [ ( 2, "#3b2a2a", 0, 0) ]
    kerning 1.0
    line_spacing 10

define e = Character("樱花", color="#ffffff", who_outlines=[ ( 2, "#3b2a2a", 0, 0) ])

image m11 = Movie(play="movie/m11.webm")
image m21 = Movie(play="movie/m21.webm")
image m22 = Movie(play="movie/m22.webm")
image m23 = Movie(play="movie/m23.webm")
image m24 = Movie(play="movie/m24.webm")
image m25 = Movie(play="movie/m25.webm")
image m26 = Movie(play="movie/m26.webm")
image m27 = Movie(play="movie/m27.webm")
image m28 = Movie(play="movie/m28.webm")
image m29 = Movie(play="movie/m29.webm")
image m31 = Movie(play="movie/m31.webm")
image m32 = Movie(play="movie/m32.webm")
image m33 = Movie(play="movie/m33.webm")
image m34 = Movie(play="movie/m34.webm")
image m35 = Movie(play="movie/m35.webm")
image m36 = Movie(play="movie/m36.webm")
image m37 = Movie(play="movie/m37.webm")
image m38 = Movie(play="movie/m38.webm")
image m39 = Movie(play="movie/m39.webm")
image m310 = Movie(play="movie/m310.webm")
image m311 = Movie(play="movie/m311.webm")
image m41 = Movie(play="movie/m41.webm")
image m42 = Movie(play="movie/m42.webm")
image m43 = Movie(play="movie/m43.webm")
image m44 = Movie(play="movie/m44.webm")
image m45 = Movie(play="movie/m45.webm")
image m46 = Movie(play="movie/m46.webm")
image m47 = Movie(play="movie/m47.webm")
image m48 = Movie(play="movie/m48.webm")
image m49 = Movie(play="movie/m49.webm")
image m410 = Movie(play="movie/m410.webm")
image m51 = Movie(play="movie/m51.webm")
image m52 = Movie(play="movie/m52.webm")
image m53 = Movie(play="movie/m53.webm")
image m54 = Movie(play="movie/m54.webm")
image m55 = Movie(play="movie/m55.webm")
image m56 = Movie(play="movie/m56.webm")
image m57 = Movie(play="movie/m57.webm")
image m58 = Movie(play="movie/m58.webm")
image m59 = Movie(play="movie/m59.webm")
image m510 = Movie(play="movie/m510.webm")
image m61 = Movie(play="movie/m61.webm")
image m62 = Movie(play="movie/m62.webm")
image m63 = Movie(play="movie/m63.webm")
image m64 = Movie(play="movie/m64.webm")
image m65 = Movie(play="movie/m65.webm")
image m66 = Movie(play="movie/m66.webm")
image m67 = Movie(play="movie/m67.webm")
image m68 = Movie(play="movie/m68.webm")
image m69 = Movie(play="movie/m69.webm")
image m71 = Movie(play="movie/m71.webm")
image m72 = Movie(play="movie/m72.webm")
image m73 = Movie(play="movie/m73.webm")
image m74 = Movie(play="movie/m74.webm")
image m75 = Movie(play="movie/m75.webm")
image m76 = Movie(play="movie/m76.webm")
image m77 = Movie(play="movie/m77.webm")
image m78 = Movie(play="movie/m78.webm")
image m79 = Movie(play="movie/m79.webm")
image m710 = Movie(play="movie/m710.webm")
image mp1 = Movie(play="movie/mp1.webm")
image mp2 = Movie(play="movie/mp2.webm")
image mp3 = Movie(play="movie/mp3.webm")
image mp4 = Movie(play="movie/mp4.webm")
image mp5 = Movie(play="movie/mp5.webm")
image mmenu = Movie(play="movie/mmenu.webm")
image m11m1 = Movie(play="movie/m11m1.webm")
image m11m2 = Movie(play="movie/m11m2.webm")
image m11m3 = Movie(play="movie/m11m3.webm")
image m11m4 = Movie(play="movie/m11m4.webm")
image m11m5 = Movie(play="movie/m11m5.webm")
image m11m6 = Movie(play="movie/m11m6.webm")
image m11m7 = Movie(play="movie/m11m7.webm")
image m22m1 = Movie(play="movie/m22m1.webm")
image m22m2 = Movie(play="movie/m22m2.webm")
image m22m3 = Movie(play="movie/m22m3.webm")
image m22m4 = Movie(play="movie/m22m4.webm")
image white_bg = ("images/white_bg.jpg")
image black_bg = ("images/black_bg.jpg")
image b11 = ("images/begin/b11.png")
image b21 = ("images/begin/b21.png")
image b22 = ("images/begin/b22.png")
image b23 = ("images/begin/b23.png")
image b24 = ("images/begin/b24.png")
image b25 = ("images/begin/b25.png")
image b26 = ("images/begin/b26.png")
image b27 = ("images/begin/b27.png")
image b28 = ("images/begin/b28.png")
image b29 = ("images/begin/b29.png")
image b31 = ("images/begin/b31.png")
image b32 = ("images/begin/b32.png")
image b33 = ("images/begin/b33.png")
image b34 = ("images/begin/b34.png")
image b35 = ("images/begin/b35.png")
image b36 = ("images/begin/b36.png")
image b37 = ("images/begin/b37.png")
image b38 = ("images/begin/b38.png")
image b39 = ("images/begin/b39.png")
image b310 = ("images/begin/b310.png")
image b311 = ("images/begin/b311.png")
image b41 = ("images/begin/b41.png")
image b42 = ("images/begin/b42.png")
image b43 = ("images/begin/b43.png")
image b44 = ("images/begin/b44.png")
image b45 = ("images/begin/b45.png")
image b46 = ("images/begin/b46.png")
image b47 = ("images/begin/b47.png")
image b48 = ("images/begin/b48.png")
image b49 = ("images/begin/b49.png")
image b410 = ("images/begin/b410.png")
image b51 = ("images/begin/b51.png")
image b52 = ("images/begin/b52.png")
image b53 = ("images/begin/b53.png")
image b54 = ("images/begin/b54.png")
image b55 = ("images/begin/b55.png")
image b56 = ("images/begin/b56.png")
image b57 = ("images/begin/b57.png")
image b58 = ("images/begin/b58.png")
image b59 = ("images/begin/b59.png")
image b510 = ("images/begin/b510.png")
image b61 = ("images/begin/b61.png")
image b62 = ("images/begin/b62.png")
image b63 = ("images/begin/b63.png")
image b64 = ("images/begin/b64.png")
image b65 = ("images/begin/b65.png")
image b66 = ("images/begin/b66.png")
image b67 = ("images/begin/b67.png")
image b68 = ("images/begin/b68.png")
image b69 = ("images/begin/b69.png")
image b71 = ("images/begin/b71.png")
image b72 = ("images/begin/b72.png")
image b73 = ("images/begin/b73.png")
image b74 = ("images/begin/b74.png")
image b75 = ("images/begin/b75.png")
image b76 = ("images/begin/b76.png")
image b77 = ("images/begin/b77.png")
image b78 = ("images/begin/b78.png")
image b79 = ("images/begin/b79.png")
image b710 = ("images/begin/b710.png")
image lomilo = ("images/lomilo.png")
image final = ("images/final.png")
image imenu = ("images/imenu.png")



# The game starts here.

label splashscreen:
    scene white_bg
    $ renpy.music.play("voice/lomilo.wav")
    show lomilo with dissolve
    $ renpy.pause(0.6)
    stop music
    hide lomilo with dissolve

    return

label start:

label cp1:

    scene white_bg
    stop music fadeout 2.0
    stop sound
    play music "voice/bird.wav"
    show mp1
    with Fade(0.0, 0.0, 1.0, color="#fff")

    "当清晨的温暖的阳光映入我的房间，一切都沉浸在白光中。"
    "又是一个无聊的周末…"
    "自从我进入大学后，我离开了家乡，开始独自生活。"
    "我不得不开始一个人生活，但我并没有因此自暴自弃…"
    play sound "voice/seding.wav"
    ""
    stop sound
    "「大哥哥，你在吗？」"
    hide mp1
    with Dissolve(1.0)
    play sound "voice/dooropen.wav"
    pause 1.5

label c11:

    play music "voice/bird.wav"
    stop sound
    scene white_bg
    show m11m1
    with Fade(0.0, 0.0, 1.0, color="#fff")
    play sound "voice/v111.wav"
    queue sound "voice/vempty.wav" loop
    e "「大哥哥，早上好！」"
    stop sound
    "「你好，樱花，今天怎么来得这么早？」"
    scene b11
    show m11m2
    play sound "voice/v112.wav"
    queue sound "voice/vempty.wav" loop
    e "「那是因为人家想早点见到你…」"
    scene b11
    show m11
    stop sound
    "樱花，是我邻居家的女孩。"
    "在我没有上课和兼职的时候，总是来陪着我。"
    "因为有她在，我才没有感到寂寞…"
    "……"
    "顺便说一下…"
    "我是一个萝莉控…"
    scene b11
    show m11m3
    play sound "voice/v113.wav"
    queue sound "voice/vempty.wav" loop
    e "「大哥哥为什么一直盯着我看，有什么问题吗？」"
    scene b11
    show m11
    stop sound
    "「没什么，我只是觉得你超级可爱。」"
    scene b11
    show m11m4
    play sound "voice/v114.wav"
    queue sound "voice/vempty.wav" loop
    e "「嘿嘿，真的吗？能得到大哥哥的夸奖，我真的超级高兴。」"
    scene b11
    show m11
    stop sound
    "「樱花，你袋子里装得是什么？」"
    scene b11
    show m11m5
    play sound "voice/v115.wav"
    queue sound "voice/vempty.wav" loop
    e "「这是我亲手做的蛋糕。」"
    scene b11
    show m11m6
    play sound "voice/v116.wav"
    queue sound "voice/vempty.wav" loop
    e "「樱花，特意给哥哥送来的哦！」"
    scene b11
    show m11
    stop sound
    "「谢谢你，一定非常美味，还愣着干什么，赶紧进屋吧！」"
    scene b11
    show m11m7
    play sound "voice/v117.wav"
    queue sound "voice/vempty.wav" loop
    e "「嗯！」"
    scene black_bg
    with Dissolve(1.0)

label cp2:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause 1.0
    play music "voice/bird_L.wav"
    show mp2
    with Fade(0.0, 0.0, 4.0, color="#000000")
    play sound "voice/v21bgvl.wav"
    ""
    scene mp3
    with Dissolve(1.0)
    ""

label c21:

    play music "voice/seo40.wav"
    play sound "voice/v211.wav"
    queue sound "voice/v21bgv.wav" loop
    scene b21
    show m21

    e "「想我了吗？你下面这个坏家伙，又硬起来了…」"
    "「樱花很认真的又开始为我舔了起来…」"
    "啊啊啊....我的龟头被少女温暖的嘴唇包裹起来了。"
    "这样的刺激是强烈的…"
    play sound "voice/v212.wav"
    queue sound "voice/v21bgv.wav" loop
    e "「舒服吗？大哥哥…唔唔...舔舐.....舔舐」"
    "樱花在我的调教下，一次次在进步…"
    "她的口交越来越好了…"
    "「简直就像一个小型的吸尘器一样…」"

label c22:

    play music "voice/seh40.wav"
    play sound "voice/v221.wav"
    queue sound "voice/vempty.wav" loop
    scene b22
    show m22m1

    e "「大哥哥，人家可是很认真的再学哦…」"
    scene b22
    show m22m2
    play sound "voice/v222.wav"
    queue sound "voice/vempty.wav" loop
    e "「希望你能喜欢我的服务…」"
    scene b22
    show m22
    stop sound
    "「看着樱花那副可爱的表情。」"
    "「我越来越兴奋了…」"
    scene b22
    show m22m3
    play sound "voice/v223.wav"
    queue sound "voice/vempty.wav" loop
    e "「我爱你，大哥哥…」"
    stop sound
    "「少女开始向我深情告白…」"
    scene b22
    show m22m4
    play sound "voice/v224.wav"
    queue sound "voice/vempty.wav" loop
    e "「感谢你一直以来为我做的一切！樱花成绩才会慢慢起来。」"
    scene b22
    show m22
    stop sound
    "「这让我想起了我们第一次相遇，好像她当时忘记带钥匙，于是，我把她领进了屋…」"
    scene black_bg
    with Dissolve(1.0)

label c23:

    play music "voice/seo30.wav"
    play sound "voice/v231.wav"
    queue sound "voice/v23bgv.wav" loop
    scene b23
    show m23
    with Dissolve(1.0)

    e "「唔唔…移动…移动、移动…」"
    "樱花的口交技术越来越熟练了，她将我的鸡巴深深的含在嘴里，然后开始晃动着小脑袋。"
    "随着我们感情的加深，在自从经过上一次的事情之后，我们再也停不下来了…"
    play sound "voice/v232.wav"
    queue sound "voice/v23bgv.wav" loop
    e "「唔唔唔…」"
    play sound "voice/v23bgv.wav" loop
    "「樱花一边帮我深喉，一边还用舌头，刺激我最敏感的位置。」"

label c24:

    play music "voice/seo30.wav"
    play sound "voice/v241.wav"
    queue sound "voice/v23bgv.wav" loop
    scene b24
    show m24

    e "「好像越来越硬了…」"
    play sound "voice/v23bgv.wav" loop
    "「对就是那，将你的头在靠近一点、」"
    play sound "voice/v242.wav"
    queue sound "voice/v23bgv.wav" loop
    e "「舔舐，舔舐…舔舐」"
    "咲花闭着眼睛，带着幸福的表情，热情帮我服务着。"
    "真是个热情的女孩。"
    "「樱花似乎已经完全沉浸其中了……」"

label c25:

    play music "voice/seo20.wav"
    play sound "voice/v251.wav"
    queue sound "voice/v25bgv.wav" loop
    scene b25
    show m25

    e "「嘻嘻，我是不是又进步了…」"
    "「是的，就是这种感觉，简直完美」"
    "樱花性感的小嘴，正在努力将我的整个鸡巴塞进她温柔的喉咙里。。"
    "我的大家伙已经抵到了她的喉咙，但她似乎丝毫，不在意的样子…"
    "「我突然有了一种罪恶感…」"
    play sound "voice/v252.wav"
    queue sound "voice/v25bgv.wav" loop
    e "「这次竟然坚持了这么久，不过我最终会你射出来的……」"

label c26:

    play music "voice/seo20.wav"
    play sound "voice/v25bgv.wav" loop
    scene b26
    show m26

    "在这间狭小的房间里，回荡着少女口水滴落为我深喉的口交声。…"
    "我快被这个淫荡的小萝莉，逼到极限了…"
    play sound "voice/v261.wav"
    queue sound "voice/v25bgv.wav" loop
    e "「唔唔唔…舔舐…舔舐…舔舐…」"

label c27:

    play music "voice/seo15.wav"
    play sound "voice/v27bgv.wav" loop
    scene b27
    show m27

    "「突然，樱花加快了节奏」"
    play sound "voice/v271.wav"
    queue sound "voice/v27bgv.wav" loop
    e "「唔唔唔…舔舐…舔舐…舔舐…」"
    "「我开始感慨，这个少女还真是潜力无限…」"
    "「我想要射精的冲动，越来越强烈了！」"
    play sound "voice/v272.wav"
    queue sound "voice/v27bgv.wav" loop
    e "「唔唔唔…舔舐…舔舐…舔舐…！」"
    "「不行了！我要射出来了....啊啊啊」"

label c28:

    play music "voice/seclio.wav" noloop
    play sound "voice/v28.wav"
    scene b28
    $ renpy.movie_cutscene("movie/m28.webm", delay=12, stop_music=False)
    scene white_bg

label c29:

    stop music
    stop sound
    scene white_bg
    play sound "voice/v291.wav"
    queue sound "voice/v29bgv.wav" loop
    show m29
    with Fade(0.0, 0.0, 2.0, color="#fff")

    e "「这味道咸咸的涩涩的」"
    play sound "voice/v29bgv.wav" loop
    "「抱歉，也许我不该射到你嘴里…」"
    "樱花继续用天真的表情看着我，她嘴里满是我的精液…"
    "看见这一幕，我下面再次开始膨胀起来了。"
    "「樱花,我们去床上吧！…」"
    play sound "voice/v292.wav"
    queue sound "voice/v29bgv.wav" loop
    e "「又要做上次那种事了吗…？」"
    play sound "voice/v29bgv.wav" loop
    "「难道不可以吗？」"
    hide m29
    with Dissolve(2.0)

label cp4:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene white_bg
    pause 1.0
    play music "voice/se40.wav"
    play sound "voice/v31bgv.wav" loop
    show mp4
    with Fade(0.0, 0.0, 4.0, color="#fff")
    ""

label c31:

    play music "voice/se40.wav"
    play sound "voice/v311.wav"
    queue sound "voice/v31bgv.wav" loop
    scene m31
    with Dissolve(1.0)

    e "「嗯啊…大哥哥那个大家伙…又进来了…」"
    play sound "voice/v31bgv.wav" loop
    "「好紧呀！…樱花的小阴道好舒服呀！……」"
    "插入的瞬间，整个鸡巴似乎都受到了强烈的压迫感。。"
    "弹力十足的肉壁，只要陷进去，就会被紧紧包裹起来…"
    "「樱花，你觉得痛吗？」"
    play sound "voice/v312.wav"
    queue sound "voice/v31bgv.wav" loop
    e "「没事的，大哥哥，你可以慢慢动了……」"
    play sound "voice/v31bgv.wav" loop
    "「我们小樱花越来越淫荡了……」"
    play sound "voice/v313.wav"
    queue sound "voice/v31bgv.wav" loop
    e "「啊…啊……啊…讨厌，还不是被你害的……」"


label c32:

    play music "voice/se40.wav"
    play sound "voice/v31bgv.wav" loop
    scene b32
    show m32

    "「樱花，你下面越来越湿了…？」"
    play sound "voice/v321.wav"
    queue sound "voice/v31bgv.wav" loop
    e "「动起来…快动起来…嗯啊…啊ぅ…啊…」"
    play sound "voice/v31bgv.wav" loop
    "「刚才不是还假装不要嘛…？」"
    play sound "voice/v322.wav"
    queue sound "voice/v31bgv.wav" loop
    e "「讨厌呀！臭哥哥…请不要再问…这种让人家…羞耻的事…」"

label c33:

    play music "voice/se40.wav"
    play sound "voice/v33bgv.wav" loop
    scene b33
    show m33

    "「动得越来越快了，你还受得了吗？…」"
    play sound "voice/v331.wav"
    queue sound "voice/v33bgv.wav" loop
    e "「可以的，大哥哥…请不要担心我…」"
    play sound "voice/v33bgv.wav" loop
    "我疯狂的向这个娇小少女发泄着心中的兽欲…"

label c34:

    play music "voice/se30.wav"
    play sound "voice/v34bgv.wav" loop
    scene b34
    show m34

    "「…樱花，这种姿势可以吗？…」"
    play sound "voice/v341.wav"
    queue sound "voice/v34bgv.wav" loop
    e "「啊啊…不行…这样……进去太多了…嗯啊…」"
    play sound "voice/v34bgv.wav" loop
    "「别担心，哥哥会慢慢来的，你一会就不觉得难受了」"
    play sound "voice/v342.wav"
    queue sound "voice/v34bgv.wav" loop
    e "「大哥哥…坚硬的大家伙，顶得人家好舒服呀！……」"
    play sound "voice/v34bgv.wav" loop
    "我抓住少女纤细的脚腕，继续向她凶横地插入。。"
    "我感到了一种前所未有的征服感。"

label c35:

    play music "voice/se30.wav"
    play sound "voice/v351.wav"
    queue sound "voice/v34bgv.wav" loop
    scene b35
    show m35

    e "「啊…啊…啊…」"
    play sound "voice/v34bgv.wav" loop
    "我以为这种近乎压倒性的姿势，疯狂向这个少女进攻着…"
    "「小樱花，现在成为我的专属物。」"
    play sound "voice/v352.wav"
    queue sound "voice/v34bgv.wav" loop
    e "「大…哥哥…真的好疼呀！…啊…啊啊……」"

label c36:

    play music "voice/se30.wav"
    play sound "voice/v36bgv.wav" loop
    scene b36
    show m36

    "「樱花…再忍耐一下就好了」"
    play sound "voice/v361.wav"
    queue sound "voice/v36bgv.wav" loop
    e "「我下面好像已经被你撑大了…」"
    play sound "voice/v362.wav"
    queue sound "voice/v36bgv.wav" loop
    e "「有一种很充实的感觉…」"
    play sound "voice/v36bgv.wav" loop
    "樱花的呻吟声，越来越陶醉了。"
    "她慢慢闭上了眼睛…好像沉浸在快乐当中。"

label c37:

    play music "voice/se20.wav"
    play sound "voice/v371.wav"
    queue sound "voice/v37bgv.wav" loop
    scene b37
    show m37

    e "「操我…快操我……大哥哥……」"
    play sound "voice/v37bgv.wav" loop
    "「淫言碎语开始从天真的樱花嘴里吐露出来。」"
    play sound "voice/v372.wav"
    queue sound "voice/v37bgv.wav" loop
    e "「虽然有些害羞…但是…我真的很高兴…」"
    play sound "voice/v37bgv.wav" loop
    "「樱花害羞的表情，真是太可爱了…」"

label c38:

    play music "voice/se20.wav"
    play sound "voice/v381.wav"
    queue sound "voice/v37bgv.wav" loop
    scene b38
    show m38

    e "「太激烈了…我快受不了…」"
    play sound "voice/v37bgv.wav" loop
    "樱花的愉悦娇喘声，让我越来越兴奋了。"
    "为了使彼此都能得到更多的快感，我更加用力扭了扭腰。"
    play sound "voice/v382.wav"
    queue sound "voice/v37bgv.wav" loop
    e "「大哥哥你好厉害呀！…樱花快被你打败了…」"
    play sound "voice/v37bgv.wav" loop
    "「樱花，你才厉害…你快把哥哥逼疯了！」"

label c39:

    play music "voice/se15.wav"
    play sound "voice/v391.wav"
    queue sound "voice/v39bgv.wav" loop
    scene b39
    show m39

    e "「受不了……太激烈了、我的脑袋都快坏掉了……」"
    play sound "voice/v39bgv.wav" loop
    "「这样就受不了…你刚才不是叫我操你吗？…」"
    play sound "voice/v392.wav"
    queue sound "voice/v39bgv.wav" loop
    e "「哎呀！……坏哥哥，你就会欺负我……」"
    play sound "voice/v39bgv.wav" loop
    "「要来了，我能射到你里面吗？」"
    play sound "voice/v393.wav"
    queue sound "voice/v39bgv.wav" loop
    e "「没关系的，大哥哥，你爱怎么样就怎么样吧！啊啊啊…」"
    play sound "voice/v39bgv.wav" loop
    "「啊啊啊……樱花……我来了！」"

label c310:

    play music "voice/seclip.wav" noloop
    play sound "voice/v310.wav"
    scene b310
    $ renpy.movie_cutscene("movie/m310.webm", delay=12, stop_music=False)
    scene white_bg

label c311:

    stop music
    stop sound
    scene white_bg
    play sound "voice/v3111.wav"
    queue sound "voice/v311bgv.wav" loop
    show m311
    with Fade(0.0, 0.0, 2.0, color="#fff")

    e "「喘气…喘气…喘气……我下面有很多很烫的白色液体进来了……」"
    play sound "voice/v311bgv.wav" loop
    "「樱花吃惊的看着这一切…」"
    "那些白色精液缓缓地从她发红的小穴里面流了出来。"
    "全部弄到了我的床上……"
    play sound "voice/v3112.wav"
    queue sound "voice/v311bgv.wav" loop
    e "「对不起，大哥哥，我把你的床弄脏的？……」"
    play sound "voice/v311bgv.wav" loop
    "「没事的，我还想一次，可以吗？……」"
    stop sound fadeout 2.0
    hide m311
    with Dissolve(2.0)


label c42:

    scene white_bg
    pause 1.0
    play music "voice/se40.wav"
    play sound "voice/v411.wav"
    queue sound "voice/v41bgv.wav" loop
    show m42
    with Fade(0.0, 0.0, 3.0, color="#fff")

    e "「啊……啊……啊…啊……」"
    play sound "voice/v41bgv.wav" loop
    "「是的，就是这样，慢慢坐下，再站起来…」"
    play sound "voice/v412.wav"
    queue sound "voice/v41bgv.wav" loop
    e "「就这是骑乘位吗，我是不是已经学会了？」"
    play sound "voice/v41bgv.wav" loop
    "「是的，你做的非常好…」"
    "在我的调教下，这个小萝莉越来越有经验了。"
    play sound "voice/v421.wav"
    queue sound "voice/v41bgv.wav" loop
    e "「真害羞，用自己的隐私部位去顶大哥哥那个硬东西……」"
    play sound "voice/v41bgv.wav" loop
    "「樱花的小穴就像一个温暖的小套子，哥哥感觉非常舒服…」"
    play sound "voice/v422.wav"
    queue sound "voice/v41bgv.wav" loop
    e "「是吗？那我就保持这个样子就好了…」"

label c43:

    play music "voice/se30.wav"
    play sound "voice/v43bgv.wav" loop
    scene b43
    show m43

    "「樱花剧烈地摇晃着自己的屁股…」"
    play sound "voice/v431.wav"
    queue sound "voice/v43bgv.wav" loop
    e "「怎么样，你喜欢我这样吗？……」"
    play sound "voice/v43bgv.wav" loop
    "她的小穴就想在邀请我一样，我下面硬得就像一块铁一样。"
    play sound "voice/v432.wav"
    queue sound "voice/v43bgv.wav" loop
    e "「大哥哥一下，就顶到人家最里面了……」"
    play sound "voice/v43bgv.wav" loop
    "「太厉害，小萝莉的小穴真让人难忘…」"

label c44:

    play music "voice/se30.wav"
    play sound "voice/v441.wav"
    queue sound "voice/v44bgv.wav" loop
    scene b44
    show m44

    e "「啊啊啊……」"
    play sound "voice/v44bgv.wav" loop
    "「樱花这种坐姿实在有点太色情了！」"
    "她就像小母狗一样趴在我的身上，然后用小穴蹂躏着我可爱的大鸡巴。"
    "就像纯情的小萝莉此时就像一位老司机一样！"
    play sound "voice/v442.wav"
    queue sound "voice/v44bgv.wav" loop
    e "「只要大哥哥喜欢……叫我做什么都愿意」"

label c45:

    play music "voice/se30.wav"
    play sound "voice/v451.wav"
    queue sound "voice/v44bgv.wav" loop
    scene b45
    show m45

    e "「动起来，为了你的性福，我也会努力的…」"
    play sound "voice/v44bgv.wav" loop
    "樱花闭上眼睛，无意识地说着下流的台词。少女芳香的气息，吹到我的脸上。"
    "「樱花，我记得我没教你这么多？」"
    play sound "voice/v452.wav"
    queue sound "voice/v44bgv.wav" loop
    e "「这是有一次，我看妈妈也这样坐到爸爸身上，所以我就学来了……」"

label c46:

    play music "voice/se20.wav"
    play sound "voice/v461.wav"
    queue sound "voice/v46bgv.wav" loop
    scene b46
    show m46

    e "「啊……大哥哥，你怎么突然就对我动手了？」"
    play sound "voice/v46bgv.wav" loop
    "「我怕樱花累坏了，所以就来帮你一把…！」"
    "我粗暴的用两只手捏着咲花的嫩嫩的屁股。"
    play sound "voice/v462.wav"
    queue sound "voice/v46bgv.wav" loop
    e "「不行了，…不行了，请您动慢一点…」"
    play sound "voice/v46bgv.wav" loop
    "「不要害羞，我知道你喜欢我这样。」"

label c47:

    play music "voice/se20.wav"
    play sound "voice/v471.wav"
    queue sound "voice/v46bgv.wav" loop
    scene b47
    show m47

    e "「这么大的家伙……在我身体里插入得这么深……」"
    play sound "voice/v46bgv.wav" loop
    "「不要担心，觉得难受的话，你可以叫出来！」"
    play sound "voice/v472.wav"
    queue sound "voice/v46bgv.wav" loop
    e "「啊、啊…啊……我的身体要快要坏掉了，哥哥的大鸡巴实在太硬了…」"

label c48:

    play music "voice/se15.wav"
    play sound "voice/v48bgv.wav" loop
    scene b48
    show m48

    "「似乎我们两个都已经到了极限了…！」"
    play sound "voice/v481.wav"
    queue sound "voice/v48bgv.wav" loop
    e "「啊…啊…太深了……」"
    play sound "voice/v48bgv.wav" loop
    "我两只手扶着她的腰，继续疯狂上下摇摆着。"
    "此时我的脑海里，只有疯狂做爱这一个念头了！"
    "「不必忍耐了，我们一起来吧！」"
    play sound "voice/v482.wav"
    queue sound "voice/v48bgv.wav" loop
    e "「啊啊，不行了，我要出来了……！」"

label c49:

    play music "voice/secli.wav" noloop
    play sound "voice/v49.wav"
    scene b49
    $ renpy.movie_cutscene("movie/m49.webm", delay=12, stop_music=False)
    scene white_bg

label c410:

    stop music
    stop sound
    scene white_bg
    play sound "voice/v4101.wav"
    queue sound "voice/v410bgv.wav" loop
    show m410
    with Fade(0.0, 0.0, 2.0, color="#fff")

    e "「喘气…喘气……喘气……」"
    play sound "voice/v410bgv.wav" loop
    "「幸苦了樱花，刚才也太疯狂了…」"
    play sound "voice/v4102.wav"
    queue sound "voice/v410bgv.wav" loop
    e "「没关系的，我觉得非常舒服…」"
    play sound "voice/v410bgv.wav" loop
    "「我也有同感。」"
    play sound "voice/v4103.wav"
    queue sound "voice/v410bgv.wav" loop
    e "「我好高兴呀！……」"
    play sound "voice/v410bgv.wav" loop
    "这光溜溜的小身板，软软的贴着我的身体。"
    "我的欲火再次被点燃了…"
    stop sound fadeout 2.0
    hide m410
    with Dissolve(3.0)


label c51:

    scene white_bg
    pause 1.0
    play music "voice/se40.wav"
    play sound "voice/v511.wav"
    queue sound "voice/v51bgv.wav" loop
    show m51
    with Fade(0.0, 0.0, 3.0, color="#fff")

    e "「好奇怪的要求，竟然让我站在桌子上……」"
    play sound "voice/v51bgv.wav" loop
    "「你难道不想体验一下，新的乐趣吗？」"
    play sound "voice/v512.wav"
    queue sound "voice/v51bgv.wav" loop
    e "「也对，那就站在上面做吧！…」"
    play sound "voice/v51bgv.wav" loop
    "「这样做比较容易。」"
    "「你只要撅着屁股就好了……」"
    "当樱花用脚尖支撑着小巧的身体时，大腿和臀部的肌肉比刚才更加紧绷了。。"
    "正好可以更加贴合我的鸡巴。"

label c52:

    play music "voice/se40.wav"
    play sound "voice/v521.wav"
    queue sound "voice/v51bgv.wav" loop
    scene b52
    show m52

    e "「大哥哥，用这样的姿势可要温柔一点哦……」"
    play sound "voice/v51bgv.wav" loop
    "「这么快就接受了，你果然是个好色的孩子…」"
    play sound "voice/v522.wav"
    queue sound "voice/v51bgv.wav" loop
    e "「讨厌，明明是大哥哥让人家用这样奇怪的姿势的…」"

label c53:

    play music "voice/se30.wav"
    play sound "voice/v53bgv.wav" loop
    scene b53
    show m53

    "「这样是不是很有趣？」"
    play sound "voice/v531.wav"
    queue sound "voice/v53bgv.wav" loop
    e "「啊啊…好奇怪的感觉，就像被你掌控着一样」"
    play sound "voice/v53bgv.wav" loop
    "「这个角度刚刚好，可以把樱花发情的样子看得清清楚楚哦。」"
    play sound "voice/v532.wav"
    queue sound "voice/v53bgv.wav" loop
    e "「大哥哥，你可以加快一点速度吗？…」"

label c54:

    play music "voice/se20.wav"
    play sound "voice/v54bgv.wav" loop
    scene b54
    show m54

    "「你可要扶稳哦，否则会摔倒的……」"
    play sound "voice/v541.wav"
    queue sound "voice/v54bgv.wav" loop
    e "「啊啊…我知道了」"
    play sound "voice/v54bgv.wav" loop
    "「刺激吧！和狗交的姿势有点像」"
    play sound "voice/v542.wav"
    queue sound "voice/v54bgv.wav" loop
    e "「嗯嗯…好害羞呀！虽然我喜欢狗，但樱花不是小狗狗。」"

label c55:

    play music "voice/se20.wav"
    play sound "voice/v54bgv.wav" loop
    scene b55
    show m55

    "樱花用剩下的一只脚艰难得支持身体。然后用小屁股努力地配合我的活塞运动。"
    "为了配合这个特别的姿势，她的全身都变得高度紧张起来。"
    "「樱花咬了咬牙艰难的硬撑着…」"
    play sound "voice/v551.wav"
    queue sound "voice/v54bgv.wav" loop
    e "「太色情了，而且我有点脚软……」"
    play sound "voice/v54bgv.wav" loop
    "「好吧！我这就让你起来。」"

label c56:

    play music "voice/se20.wav"
    play sound "voice/v561.wav"
    queue sound "voice/v56bgv.wav" loop
    scene b56
    show m56

    e "「太厉害了，大哥哥似乎比上次更强了…」"
    play sound "voice/v56bgv.wav" loop
    "「怎么样？是不是比上次的体验更好呀？……」"
    "我用力的干着这个娇艳的小穴。"
    play sound "voice/v562.wav"
    queue sound "voice/v56bgv.wav" loop
    e "「啊啊啊……太强了」"

label c57:

    play music "voice/se20.wav"
    play sound "voice/v56bgv.wav" loop
    scene b57
    show m57

    "从阴茎传来的强烈快感不断涌入樱花大脑，她再也不去考虑其他的事呢！。。"
    play sound "voice/v571.wav"
    queue sound "voice/v56bgv.wav" loop
    e "「再快点…樱花，好喜欢你这样」"
    play sound "voice/v56bgv.wav" loop
    "「是吗？那我就继续了……」"
    play sound "voice/v572.wav"
    queue sound "voice/v56bgv.wav" loop
    e "「大哥哥呀！别这样一直戳著那里……实在太丢脸了」"

label c58:

    play music "voice/se15.wav"
    play sound "voice/v58bgv.wav" loop
    scene b58
    show m58

    "「竟然发出如此下流的声音…可爱的屁股在眼前这样摇动着…」"
    play sound "voice/v581.wav"
    queue sound "voice/v58bgv.wav" loop
    e "「哇，哇，哇，呜啊……已经不行了啊…」"
    play sound "voice/v58bgv.wav" loop
    "「我也是的，你的小淫穴又要让我射出来了！」"
    play sound "voice/v582.wav"
    queue sound "voice/v58bgv.wav" loop
    e "「射在里面吗？我也不想在等了………！」"
    play sound "voice/v58bgv.wav" loop
    "「噢啊啊!又来了…又要射出来了……！」"

label c59:

    play music "voice/secli.wav" noloop
    play sound "voice/v59.wav"
    scene b59
    $ renpy.movie_cutscene("movie/m59.webm", delay=12, stop_music=False)
    scene white_bg

label c510:

    stop music
    stop sound
    scene white_bg
    play sound "voice/v5101.wav"
    queue sound "voice/v510bgv.wav" loop
    show m510
    with Fade(0.0, 0.0, 2.0, color="#fff")

    e "「哎呀，我的脚都麻了…」"
    play sound "voice/v510bgv.wav" loop
    "「什么嘛，你明明一副很陶醉的样子。」"
    play sound "voice/v5102.wav"
    queue sound "voice/v510bgv.wav" loop
    e "「是真的，人家都已经站不起了…」"
    play sound "voice/v510bgv.wav" loop
    "樱花晃动了一下身体，精液从她小穴口流了出来…"
    "「非常棒，下次也要保持这样的姿势」"
    play sound "voice/v5103.wav"
    queue sound "voice/v510bgv.wav" loop
    e "「但是，大哥哥，我们能坐着来吗？……」"
    stop sound fadeout 2.0
    hide m510
    with Dissolve(3.0)


label c61:

    scene white_bg
    pause 1.0
    play music "voice/se40.wav"
    play sound "voice/v611.wav"
    queue sound "voice/v61bgv.wav" loop
    show m61
    with Fade(0.0, 0.0, 3.0, color="#fff")

    e "「嗯…啊…啊……啊……」"
    play sound "voice/v61bgv.wav" loop
    "「我们的小樱花越来越熟练了？」"
    play sound "voice/v612.wav"
    queue sound "voice/v61bgv.wav" loop
    e "「是的，坐在大哥哥腿上的感觉真是太舒服了……」"
    play sound "voice/v61bgv.wav" loop
    "果然，我是对的，你就像喜欢这样被我抱着。"
    "每天我放下樱花纤细而柔软的身体，她的紧蹦蹦的小阴道就紧紧地缠绕在我的阴茎上…"

label c62:

    play music "voice/se40.wav"
    play sound "voice/v621.wav"
    queue sound "voice/v61bgv.wav" loop
    scene b62
    show m62

    e "「大哥哥的耐力还真好……」"
    play sound "voice/v61bgv.wav" loop
    "「那是因为小樱花实在太诱人了。」"
    "「我们的对话非常自然，就是经常在一起的情侣一样…」"
    play sound "voice/v622.wav"
    queue sound "voice/v61bgv.wav" loop
    e "「我真的好喜欢…和大哥哥一起做爱呀！」"

label c63:

    play music "voice/se30.wav"
    play sound "voice/v631.wav"
    queue sound "voice/v63bgv.wav" loop
    scene b63
    show m63

    e "「大哥哥，等我长大了你会娶我吗？…」"
    play sound "voice/v63bgv.wav" loop
    "「当然会，我只爱你一个…」"
    "「你看我们的性生活是多么和谐呀！……」"
    play sound "voice/v632.wav"
    queue sound "voice/v63bgv.wav" loop
    e "「嗯…我相信你……请让我更舒服吧！…」"

label c64:

    play music "voice/se20.wav"
    play sound "voice/v641.wav"
    queue sound "voice/v64bgv.wav" loop
    scene b64
    show m64

    e "「哇啊啊，我在空中了…」"
    play sound "voice/v64bgv.wav" loop
    "「放心吧！我不会让你掉下去…」"
    "樱花小小的身体，几乎让我感受不到什么重量。"
    "这样的姿势只会让我们更加亲密。"
    play sound "voice/v642.wav"
    queue sound "voice/v64bgv.wav" loop
    e "「嗯…啊啊……这种感觉就像做跷跷板一样…」"

label c65:

    play music "voice/se20.wav"
    play sound "voice/v64bgv.wav" loop
    scene b65
    show m65

    "「我们两个人都爱上了这种欲罢不能的感觉。」"
    play sound "voice/v651.wav"
    queue sound "voice/v64bgv.wav" loop
    e "「轻点，轻点，都快顶到人家肚子里面了……」"
    play sound "voice/v64bgv.wav" loop
    "「好戏才刚刚开始哦…」"

label c66:

    play music "voice/se20.wav"
    play sound "voice/v661.wav"
    queue sound "voice/v66bgv.wav" loop
    scene b66
    show m66

    e "「嗯…啊、啊、嗯…嗯……哦，哦…啊…嗯啊…啊啊啊……」"
    play sound "voice/v66bgv.wav" loop
    "「樱花忘情地呻吟着…！」"
    "我继续保持这样的抽擦速度。"
    "「啪啪啪…整个屋子都是我们肉体碰撞的声音」"
    play sound "voice/v662.wav"
    queue sound "voice/v66bgv.wav" loop
    e "「太丢人了，我在空中被你侵犯，但是又觉得非常刺激……」"

label c67:

    play music "voice/se15.wav"
    play sound "voice/v67bgv.wav" loop
    scene b67
    show m67

    "「看着这张清纯的脸，我加快了速度……！」"
    play sound "voice/v671.wav"
    queue sound "voice/v67bgv.wav" loop
    e "「嗯啊啊……，这样的速度实在太快了，啊啊…不行…」"
    play sound "voice/v67bgv.wav" loop
    "「樱花开始有些吃不消了……！」"
    play sound "voice/v672.wav"
    queue sound "voice/v67bgv.wav" loop
    e "「大哥哥，我不行了……我真的不行了」"
    play sound "voice/v67bgv.wav" loop
    "「要出来了，我又要射出来了！」"

label c68:

    play music "voice/secli.wav" noloop
    play sound "voice/v68.wav"
    scene b68
    $ renpy.movie_cutscene("movie/m68.webm", delay=12, stop_music=False)
    scene white_bg

label c69:

    stop music
    stop sound
    scene white_bg
    play sound "voice/v691.wav"
    queue sound "voice/v69bgv.wav" loop
    show m69
    with Fade(0.0, 0.0, 2.0, color="#fff")

    e "「我肚子里，充满那些白花花的液体……」"
    play sound "voice/v69bgv.wav" loop
    "「舒服吗？特别是射出来的一瞬间对吗？…」"
    play sound "voice/v692.wav"
    queue sound "voice/v69bgv.wav" loop
    e "「有一种被释放的感觉…」"
    play sound "voice/v69bgv.wav" loop
    "我也是，真想一直跟你做下去…"
    stop sound fadeout 2.0
    hide m69
    with Dissolve(3.0)


label c71:

    scene white_bg
    pause 1.0
    play music "voice/se40.wav"
    play sound "voice/v711.wav"
    queue sound "voice/v71bgv.wav" loop
    show m71
    with Fade(0.0, 0.0, 3.0, color="#fff")

    e "「又要来吗？我的身体已经吃不消了……」"
    play sound "voice/v71bgv.wav" loop
    "「再来一次吧！我保证这是最后一次…」"
    play sound "voice/v712.wav"
    queue sound "voice/v71bgv.wav" loop
    e "「好吧！大哥哥……我会尽量忍耐的」"
    play sound "voice/v71bgv.wav" loop
    "放心吧！这次我一样会很温柔的…"
    "我再次向里面的嫩肉推进了。"

label c72:

    play music "voice/se40.wav"
    play sound "voice/v721.wav"
    queue sound "voice/v71bgv.wav" loop
    scene b72
    show m72

    e "「哇哦…我感觉越来越热了…」"
    play sound "voice/v71bgv.wav" loop
    "「这是正常现象，看来樱花已经进入状态了…」"
    "樱花白皙的皮肤在阳光照射下露出粉红色的光泽。简直好像一件精美的玉器一样。"
    "樱花的娇嫩的小嘴，再次发出了极具诱惑力的声音…"
    play sound "voice/v722.wav"
    queue sound "voice/v71bgv.wav" loop
    e "「我好像变得越来越好色了……」"

label c73:

    play music "voice/se30.wav"
    play sound "voice/v731.wav"
    queue sound "voice/v73bgv.wav" loop
    scene b73
    show m73

    e "「这种姿势就是大哥哥，你上次说的老牛推车吗？…」"
    play sound "voice/v73bgv.wav" loop
    "「没错的，樱花真的很聪明，这是我最喜欢的姿势。抬起你的臀部，做出像小狗一样的性感动作。」"
    play sound "voice/v732.wav"
    queue sound "voice/v73bgv.wav" loop
    e "「拜托，你能不能别说出来，人家好害羞呀…」"
    play sound "voice/v73bgv.wav" loop
    "「将你的小屁股抬高，你会慢慢习惯的。」"
    play sound "voice/v733.wav"
    queue sound "voice/v73bgv.wav" loop
    e "「啊…啊……慢点，慢点，你慢点……」"

label c74:

    play music "voice/se30.wav"
    play sound "voice/v73bgv.wav" loop
    scene b74
    show m74

    "小萝莉喘着粗气的声音，周围全身肉棒和阴道互相摩擦的水声…"
    "「樱花，用小狗的做爱方式做爱舒服吗？」"
    play sound "voice/v741.wav"
    queue sound "voice/v73bgv.wav" loop
    e "「啊啊啊…很舒服……我好喜欢…这样……」"
    play sound "voice/v73bgv.wav" loop
    "「你哪里舒服了？」"
    play sound "voice/v742.wav"
    queue sound "voice/v73bgv.wav" loop
    e "「被大哥哥插入进入……搅动着我小穴的时候」"

label c75:

    play music "voice/se20.wav"
    play sound "voice/v75bgv.wav" loop
    scene b75
    show m75

    "「这样抓着你的手，也没关系吧？」"
    play sound "voice/v751.wav"
    queue sound "voice/v75bgv.wav" loop
    e "「这个太…啊啊啊……不过也不是不可以」"
    play sound "voice/v75bgv.wav" loop
    "在强烈的刺激下，樱花的阴道已经完全湿润了，这样显得更加紧绷，就能更加夹紧我的阴茎了。"
    "「不好好欺负一下这个外表单纯，内心却极度淫荡的小萝莉……都觉得对不起她」"
    play sound "voice/v752.wav"
    queue sound "voice/v75bgv.wav" loop
    e "「好舒服呀！大哥哥…就这样一直动吧！」"

label c76:

    play music "voice/se20.wav"
    play sound "voice/v761.wav"
    queue sound "voice/v76bgv.wav" loop
    scene b76
    show m76

    e "「太厉害了……我被你弄得全身都在发抖」"
    play sound "voice/v76bgv.wav" loop
    "鸡巴粗暴地抽插着她的深处。多次碰到柔软有弹性的肉壁，然后每次都顶了回来…"
    "「啊，这样就是打开樱花子宫的入口…也就是我们将来孕育孩子的地方」"
    play sound "voice/v762.wav"
    queue sound "voice/v76bgv.wav" loop
    e "「将来孕育孩子的地方？…」"

label c77:

    play music "voice/se20.wav"
    play sound "voice/v771.wav"
    queue sound "voice/v76bgv.wav" loop
    scene b77
    show m77

    e "「太幸苦了……孕育孩子真是太幸苦了」"
    play sound "voice/v76bgv.wav" loop
    "别担心，你现在年纪还小，是不会怀孕的。"
    "我疯狂地对着，她的小小嫩穴，输出着…"
    "「樱花，这样可爱而性感的身体…根本让我停不下来，我将再次填满你盛开的小子宫！」"
    play sound "voice/v772.wav"
    queue sound "voice/v76bgv.wav" loop
    e "「来吧！大哥哥…快填满我吧！」"

label c78:

    play music "voice/se15.wav"
    play sound "voice/v78bgv.wav" loop
    scene b78
    show m78

    "「樱花的乞求声，再次将这次性爱带入了高潮！」"
    "「要来了，我真的射进来了……！」"
    play sound "voice/v781.wav"
    queue sound "voice/v78bgv.wav" loop
    e "「嗯…可以的，大哥哥，快给我吧！」"
    play sound "voice/v78bgv.wav" loop
    "「太好了，我这次还要将你的小子宫填满！」"
    play sound "voice/v782.wav"
    queue sound "voice/v78bgv.wav" loop
    e "「啊啊啊，我也要来了！」"
    play sound "voice/v78bgv.wav" loop
    "「我们一起进入高潮吧！」"

label c79:

    play music "voice/secli.wav" noloop
    play sound "voice/v79.wav"
    scene b79
    $ renpy.movie_cutscene("movie/m79.webm", delay=12, stop_music=False)
    scene white_bg

label c710:

    stop music
    stop sound
    scene white_bg
    play sound "voice/v7101.wav"
    queue sound "voice/v710bgv.wav" loop
    show m710
    with Fade(0.0, 0.0, 2.0, color="#fff")

    e "「喘气……喘气，又有这么多黏糊糊的东西」"
    play sound "voice/v710bgv.wav" loop
    "「对不起，樱花，我没有控制住自己。」"
    play sound "voice/v7102.wav"
    queue sound "voice/v710bgv.wav" loop
    e "「没关系的，我们已经是爱人了。记得，等我长大了一定要娶我哦」"
    play sound "voice/v7103.wav"
    queue sound "voice/v710bgv.wav" loop
    e "「大哥哥，我们一起拉钩钩…」"
    stop sound
    scene white_bg
    with Dissolve(1.5)

label cp5:


    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause 0.5
    play music "voice/bird_L.wav"
    show mp5
    with Fade(0.0, 0.0, 1.5, color="#ffffff")
    play sound "voice/v7104.wav"
    e "「大哥哥，现在可以了吧？我们一起吃蛋糕吧！」"
    stop sound
    "「吃什么蛋糕，我更想吃你…再来帮我舔鸡巴吧！」"
    play sound "voice/v71052.wav"
    queue sound "voice/v41bgv.wav" loop
    e "「可，可是，不行呀！已经来了这么多次，我会死掉的。 」"
    play music "voice/se40.wav"
    play sound "voice/v41bgv.wav" loop
    ""
    stop music fadeout 7.0
    stop sound fadeout 7.0
    scene white_bg
    with Dissolve(1.0)
    pause 1.0
    scene final
    with Dissolve(1.0)
    pause 2.0
    scene white_bg
    with Dissolve(2.0)
    pause 1.0

    # This ends the game.

$ renpy.full_restart()
