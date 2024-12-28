from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 840)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 0, 61, 71))
        self.logo.setStyleSheet("image:url(:/images/images/logofolha.png)")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 931, 71))
        self.label_2.setStyleSheet("background-color: rgb(0, 75, 63);\n"
"\n"
"\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.labelBemvindo = QtWidgets.QLabel(self.centralwidget)
        self.labelBemvindo.setGeometry(QtCore.QRect(70, 80, 791, 161))
        self.labelBemvindo.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"")
        self.labelBemvindo.setObjectName("labelBemvindo")
        self.LineBuscar = QtWidgets.QLineEdit(self.centralwidget)
        self.LineBuscar.setGeometry(QtCore.QRect(190, 240, 541, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LineBuscar.setFont(font)
        self.LineBuscar.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.LineBuscar.setStyleSheet("QLineEdit {\n"
" border: 1px solid #CCCCCC;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QLineEdit ::focus {\n"
"    background-color: rgb(0, 75, 63);\n"
"}")
        self.LineBuscar.setFrame(True)
        self.LineBuscar.setClearButtonEnabled(False)
        self.LineBuscar.setObjectName("LineBuscar")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(350, 380, 241, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 670, 931, 161))
        self.label_8.setStyleSheet("background-color: rgb(0, 75, 63);\n"
"\n"
"\n"
"")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 70, 931, 601))
        self.label_3.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.labelFrase = QtWidgets.QLabel(self.centralwidget)
        self.labelFrase.setGeometry(QtCore.QRect(310, 190, 301, 21))
        self.labelFrase.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color:#6E7683;")
        self.labelFrase.setObjectName("labelFrase")
        self.nomeLogo = QtWidgets.QPushButton(self.centralwidget)
        self.nomeLogo.setGeometry(QtCore.QRect(60, 10, 181, 51))
        self.nomeLogo.setStyleSheet("\n"
"QPushButton {  \n"
"    background-color: rgb(0, 75, 63);\n"
"   font: 15pt \"Cooper Black\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    \n"
"       \n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 75, 63);\n"
"   font: 15pt \"Cooper Black\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"   \n"
"border: 1px solid #CCCCCC;\n"
"box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
"background-color: #D6D6D6; /* Fundo mais escuro */\n"
"   \n"
"    transform: translateY(2px); /* Deslocamento para baixo */\n"
"   \n"
"}\n"
"\n"
"\n"
"")
        self.nomeLogo.setObjectName("nomeLogo")
        self.botaoBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoBuscar.setGeometry(QtCore.QRect(690, 240, 41, 41))
        self.botaoBuscar.setStyleSheet("QPushButton {  \n"
"    background-color: rgb(0, 75, 63);\n"
"     border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/lupa-arredondada.png); /* Caminho da imagem */\n"
"      \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: #E5E5E5;\n"
"   \n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/lupa-arredondada.png); /* Caminho da imagem */\n"
"    \n"
"border: 1px solid #CCCCCC;\n"
"box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #E5E5E5;\n"
"    \n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/lupa-arredondada.png); /* Caminho da imagem */\n"
"    \n"
"border: 1px solid #CCCCCC;\n"
"box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
"background-color: #D6D6D6; /* Fundo mais escuro */\n"
"    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.2); /* Menor sombra */\n"
"    transform: translateY(2px); /* Deslocamento para baixo */\n"
"    border: 1px solid #AAAAAA; /* Borda mais escura */\n"
"}\n"
"\n"
"\n"
"")
        self.botaoBuscar.setText("")
        self.botaoBuscar.setObjectName("botaoBuscar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 390, 341, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(590, 390, 341, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 300, 821, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BotaoReservar = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.BotaoReservar.setStyleSheet("QPushButton{  \n"
"background-color: rgb(0, 75, 63);\n"
"font: 9pt \"Cooper Black\"; /* Fonte e tamanho */\n"
"color: rgb(255, 255, 255); /* Cor do texto */\n"
"text-align: left; /* Texto alinhado à esquerda */\n"
"border-radius: 8px; /* Bordas arredondadas */\n"
"padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */ \n"
"image: url(:/images/images/001-caixa.png); /* Caminho da imagem */\n"
"image-position:right; /* Posiciona a imagem no centro da área disponível */\n"
"background-size: 32px 32px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(156, 180, 172);\n"
"font: 9pt \"Cooper Black\"; /* Fonte e tamanho */\n"
"color: rgb(255, 255, 255); /* Cor do texto */\n"
"text-align: left; /* Texto alinhado à esquerda */\n"
"border-radius: 8px; /* Bordas arredondadas */\n"
"padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */ \n"
"image: url(:/images/images/001-caixa.png); /* Caminho da imagem */\n"
"image-position:right; /* Posiciona a imagem no centro da área disponível */\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(156, 180, 172);\n"
"font: 8pt \"Cooper Black\"; /* Fonte e tamanho */\n"
"color: rgb(255, 255, 255); /* Cor do texto */\n"
"text-align: left; /* Texto alinhado à esquerda */\n"
"border-radius: 8px; /* Bordas arredondadas */\n"
"padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */ \n"
"image: url(:/images/images/001-caixa.png); /* Caminho da imagem */\n"
"image-position:right; /* Posiciona a imagem no centro da área disponível */\n"
"}\n"
"\n"
"\n"
"")
        self.BotaoReservar.setObjectName("BotaoReservar")
        self.horizontalLayout_2.addWidget(self.BotaoReservar)
        self.botaoOfertas = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 75, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 75, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 75, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 75, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 75, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 75, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 75, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 75, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 75, 63))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.botaoOfertas.setPalette(palette)
        self.botaoOfertas.setMouseTracking(True)
        self.botaoOfertas.setTabletTracking(True)
        self.botaoOfertas.setFocusPolicy(QtCore.Qt.NoFocus)
        self.botaoOfertas.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.botaoOfertas.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botaoOfertas.setStyleSheet("QPushButton{  \n"
"background-color: rgb(0, 75, 63);\n"
"font: 9pt \"Cooper Black\"; /* Fonte e tamanho */\n"
"color: rgb(255, 255, 255); /* Cor do texto */\n"
"text-align: left; /* Texto alinhado à esquerda */\n"
"border-radius: 8px; /* Bordas arredondadas */\n"
"padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */ \n"
"image: url(:/images/images/002-calendrio.png); /* Caminho da imagem */\n"
"image-position:right; /* Posiciona a imagem no centro da área disponível */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(156, 180, 172);\n"
"font: 9pt \"Cooper Black\"; /* Fonte e tamanho */\n"
"color: rgb(255, 255, 255); /* Cor do texto */\n"
"text-align: left; /* Texto alinhado à esquerda */\n"
"border-radius: 8px; /* Bordas arredondadas */\n"
"padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */ \n"
"image: url(:/images/images/002-calendrio.png); /* Caminho da imagem */\n"
"image-position:right; /* Posiciona a imagem no centro da área disponível */\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(156, 180, 172);\n"
"font: 8pt \"Cooper Black\"; /* Fonte e tamanho */\n"
"color: rgb(255, 255, 255); /* Cor do texto */\n"
"text-align: left; /* Texto alinhado à esquerda */\n"
"border-radius: 8px; /* Bordas arredondadas */\n"
"padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */ \n"
"image: url(:/images/images/002-calendrio.png); /* Caminho da imagem */\n"
"image-position:right; /* Posiciona a imagem no centro da área disponível */\n"
"}\n"
"\n"
"\n"
"")
        self.botaoOfertas.setCheckable(False)
        self.botaoOfertas.setAutoDefault(False)
        self.botaoOfertas.setObjectName("botaoOfertas")
        self.horizontalLayout_2.addWidget(self.botaoOfertas)
        self.botaoChat = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.botaoChat.setStyleSheet("QPushButton{  \n"
"background-color: rgb(0, 75, 63);\n"
"font: 9pt \"Cooper Black\"; /* Fonte e tamanho */\n"
"color: rgb(255, 255, 255); /* Cor do texto */\n"
"text-align: left; /* Texto alinhado à esquerda */\n"
"border-radius: 8px; /* Bordas arredondadas */\n"
"padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */ \n"
"image: url(:/images/images/003-balo-de-fala.png); /* Caminho da imagem */\n"
"image-position:right; /* Posiciona a imagem no centro da área disponível */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(156, 180, 172);\n"
"font: 9pt \"Cooper Black\"; /* Fonte e tamanho */\n"
"color: rgb(255, 255, 255); /* Cor do texto */\n"
"text-align: left; /* Texto alinhado à esquerda */\n"
"border-radius: 8px; /* Bordas arredondadas */\n"
"padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */ \n"
"image: url(:/images/images/003-balo-de-fala.png); /* Caminho da imagem */\n"
"image-position:right; /* Posiciona a imagem no centro da área disponível */\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(156, 180, 172);\n"
"font: 8pt \"Cooper Black\"; /* Fonte e tamanho */\n"
"color: rgb(255, 255, 255); /* Cor do texto */\n"
"text-align: left; /* Texto alinhado à esquerda */\n"
"border-radius: 8px; /* Bordas arredondadas */\n"
"padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */ \n"
"image: url(:/images/images/003-balo-de-fala.png); /* Caminho da imagem */\n"
"image-position:right; /* Posiciona a imagem no centro da área disponível */\n"
"}\n"
"\n"
"\n"
"")
        self.botaoChat.setObjectName("botaoChat")
        self.horizontalLayout_2.addWidget(self.botaoChat)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(80, 430, 161, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 161, 121))
        self.label.setStyleSheet("background-color: rgb(165, 165, 165);\n"
"border-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(110, 10, 41, 31))
        self.label_6.setStyleSheet("border-radius: 8px;\n"
"background-color: rgb(255, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"padding:2px;")
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 131, 31))
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(10, 150, 101, 21))
        self.label_9.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 75, 63)")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(70, 150, 55, 21))
        self.label_10.setStyleSheet("font: 6pt \"MS Shell Dlg 2\";\n"
"text-decoration: line-through;")
        self.label_10.setObjectName("label_10")
        self.BotaoAddCesta = QtWidgets.QPushButton(self.frame)
        self.BotaoAddCesta.setGeometry(QtCore.QRect(30, 180, 101, 31))
        self.BotaoAddCesta.setStyleSheet("QPushButton {  \n"
"    background-color: rgb(0, 75, 63);\n"
"    font: 75 7pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/001-shopping-basket.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: #E5E5E5;\n"
"    font: 75 7pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/001-shopping-basket.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */\n"
"border: 1px solid #CCCCCC;\n"
"box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #E5E5E5;\n"
"    font: 75 7pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/001-shopping-basket.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */\n"
"border: 1px solid #CCCCCC;\n"
"box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
"background-color: #D6D6D6; /* Fundo mais escuro */\n"
"    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.2); /* Menor sombra */\n"
"    transform: translateY(2px); /* Deslocamento para baixo */\n"
"    border: 1px solid #AAAAAA; /* Borda mais escura */\n"
"}\n"
"\n"
"\n"
"")
        self.BotaoAddCesta.setObjectName("BotaoAddCesta")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(290, 430, 161, 211))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(110, 10, 41, 31))
        self.label_11.setStyleSheet("border-radius: 8px;\n"
"background-color: rgb(255, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"padding:2px;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(10, 120, 131, 31))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(10, 150, 101, 21))
        self.label_13.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 75, 63)")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(70, 150, 55, 21))
        self.label_14.setStyleSheet("font: 6pt \"MS Shell Dlg 2\";\n"
"text-decoration: line-through;")
        self.label_14.setObjectName("label_14")
        self.BotaoAddCesta_2 = QtWidgets.QPushButton(self.frame_2)
        self.BotaoAddCesta_2.setGeometry(QtCore.QRect(30, 180, 101, 31))
        self.BotaoAddCesta_2.setStyleSheet("QPushButton {  \n"
"    background-color: rgb(0, 75, 63);\n"
"    font: 75 7pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/001-shopping-basket.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: #E5E5E5;\n"
"    font: 75 7pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/001-shopping-basket.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */\n"
"border: 1px solid #CCCCCC;\n"
"box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #E5E5E5;\n"
"    font: 75 7pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/001-shopping-basket.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */\n"
"border: 1px solid #CCCCCC;\n"
"box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
"background-color: #D6D6D6; /* Fundo mais escuro */\n"
"    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.2); /* Menor sombra */\n"
"    transform: translateY(2px); /* Deslocamento para baixo */\n"
"    border: 1px solid #AAAAAA; /* Borda mais escura */\n"
"}\n"
"\n"
"\n"
"")
        self.BotaoAddCesta_2.setObjectName("BotaoAddCesta_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 161, 121))
        self.label_4.setStyleSheet("background-color: rgb(165, 165, 165);\n"
"border-color: rgb(0, 0, 0);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.BotaoAddCesta_2.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(490, 430, 161, 211))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(110, 10, 41, 31))
        self.label_15.setStyleSheet("border-radius: 8px;\n"
"background-color: rgb(255, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"padding:2px;")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(10, 120, 131, 31))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(10, 150, 101, 21))
        self.label_17.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 75, 63)")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_3)
        self.label_18.setGeometry(QtCore.QRect(70, 150, 55, 21))
        self.label_18.setStyleSheet("font: 6pt \"MS Shell Dlg 2\";\n"
"text-decoration: line-through;")
        self.label_18.setObjectName("label_18")
        self.BotaoAddCesta_3 = QtWidgets.QPushButton(self.frame_3)
        self.BotaoAddCesta_3.setGeometry(QtCore.QRect(30, 180, 101, 31))
        self.BotaoAddCesta_3.setStyleSheet("QPushButton {  \n"
"    background-color: rgb(0, 75, 63);\n"
"    font: 75 7pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/001-shopping-basket.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: #E5E5E5;\n"
"    font: 75 7pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/001-shopping-basket.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */\n"
"border: 1px solid #CCCCCC;\n"
"box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #E5E5E5;\n"
"    font: 75 7pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/001-shopping-basket.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */\n"
"border: 1px solid #CCCCCC;\n"
"box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
"background-color: #D6D6D6; /* Fundo mais escuro */\n"
"    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.2); /* Menor sombra */\n"
"    transform: translateY(2px); /* Deslocamento para baixo */\n"
"    border: 1px solid #AAAAAA; /* Borda mais escura */\n"
"}\n"
"\n"
"\n"
"")
        self.BotaoAddCesta_3.setObjectName("BotaoAddCesta_3")
        self.label_19 = QtWidgets.QLabel(self.frame_3)
        self.label_19.setGeometry(QtCore.QRect(0, 0, 161, 121))
        self.label_19.setStyleSheet("background-color: rgb(165, 165, 165);\n"
"border-color: rgb(0, 0, 0);")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(690, 430, 161, 211))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_20 = QtWidgets.QLabel(self.frame_4)
        self.label_20.setGeometry(QtCore.QRect(110, 10, 41, 31))
        self.label_20.setStyleSheet("border-radius: 8px;\n"
"background-color: rgb(255, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"padding:2px;")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame_4)
        self.label_21.setGeometry(QtCore.QRect(10, 120, 131, 31))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_4)
        self.label_22.setGeometry(QtCore.QRect(10, 150, 101, 21))
        self.label_22.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 75, 63)")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_4)
        self.label_23.setGeometry(QtCore.QRect(70, 150, 55, 21))
        self.label_23.setStyleSheet("font: 6pt \"MS Shell Dlg 2\";\n"
"text-decoration: line-through;")
        self.label_23.setObjectName("label_23")
        self.BotaoAddCesta_4 = QtWidgets.QPushButton(self.frame_4)
        self.BotaoAddCesta_4.setGeometry(QtCore.QRect(30, 180, 101, 31))
        self.BotaoAddCesta_4.setStyleSheet("QPushButton {  \n"
"    background-color: rgb(0, 75, 63);\n"
"    font: 75 7pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/001-shopping-basket.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: #E5E5E5;\n"
"    font: 75 7pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/001-shopping-basket.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */\n"
"border: 1px solid #CCCCCC;\n"
"box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #E5E5E5;\n"
"    font: 75 7pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/001-shopping-basket.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */\n"
"border: 1px solid #CCCCCC;\n"
"box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
"background-color: #D6D6D6; /* Fundo mais escuro */\n"
"    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.2); /* Menor sombra */\n"
"    transform: translateY(2px); /* Deslocamento para baixo */\n"
"    border: 1px solid #AAAAAA; /* Borda mais escura */\n"
"}\n"
"\n"
"\n"
"")
        self.BotaoAddCesta_4.setObjectName("BotaoAddCesta_4")
        self.label_24 = QtWidgets.QLabel(self.frame_4)
        self.label_24.setGeometry(QtCore.QRect(0, 0, 161, 121))
        self.label_24.setStyleSheet("background-color: rgb(165, 165, 165);\n"
"border-color: rgb(0, 0, 0);")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.botaoCesta = QtWidgets.QPushButton(self.centralwidget)
        self.botaoCesta.setGeometry(QtCore.QRect(818, 20, 91, 38))
        self.botaoCesta.setStyleSheet("QPushButton {  \n"
"    background-color: rgb(0, 75, 63);\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/001-shopping-basket.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: #E5E5E5;\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/001-shopping-basket.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */\n"
"border: 1px solid #CCCCCC;\n"
"box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #E5E5E5;\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/001-shopping-basket.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */\n"
"border: 1px solid #CCCCCC;\n"
"box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
"background-color: #D6D6D6; /* Fundo mais escuro */\n"
"    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.2); /* Menor sombra */\n"
"    transform: translateY(2px); /* Deslocamento para baixo */\n"
"    border: 1px solid #AAAAAA; /* Borda mais escura */\n"
"}\n"
"\n"
"\n"
"")
        self.botaoCesta.setObjectName("botaoCesta")
        self.botaoEntrar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoEntrar.setGeometry(QtCore.QRect(530, 20, 101, 38))
        self.botaoEntrar.setStyleSheet("QPushButton {  \n"
"    background-color: rgb(0, 75, 63);\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/002-entrar.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: #E5E5E5;\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/002-entrar.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */\n"
"border: 1px solid #CCCCCC;\n"
"box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #E5E5E5;\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/002-entrar.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */\n"
"border: 1px solid #CCCCCC;\n"
"box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
"background-color: #D6D6D6; /* Fundo mais escuro */\n"
"    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.2); /* Menor sombra */\n"
"    transform: translateY(2px); /* Deslocamento para baixo */\n"
"    border: 1px solid #AAAAAA; /* Borda mais escura */\n"
"}\n"
"\n"
"\n"
"")
        self.botaoEntrar.setObjectName("botaoEntrar")
        self.botaoCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoCadastrar.setGeometry(QtCore.QRect(660, 20, 123, 38))
        self.botaoCadastrar.setStyleSheet("QPushButton {  \n"
"    background-color: rgb(0, 75, 63);\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/003-pessoa.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color: #E5E5E5;\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/003-pessoa.png); /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */\n"
"border: 1px solid #CCCCCC;\n"
"box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #E5E5E5;\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255); /* Cor do texto */\n"
"    border-radius: 8px; /* Bordas arredondadas */\n"
"    padding: 10px; /* Padding interno (topo, direita, fundo, esquerda) */\n"
"    image: url(:/images/images/003-pessoa.png);; /* Caminho da imagem */\n"
"    image-position:left;   \n"
"    text-align: right; /* Centraliza o texto */\n"
"border: 1px solid #CCCCCC;\n"
"box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra leve */\n"
"background-color: #D6D6D6; /* Fundo mais escuro */\n"
"    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.2); /* Menor sombra */\n"
"    transform: translateY(2px); /* Deslocamento para baixo */\n"
"    border: 1px solid #AAAAAA; /* Borda mais escura */\n"
"}\n"
"\n"
"\n"
"")
        self.botaoCadastrar.setObjectName("botaoCadastrar")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(20, 680, 321, 131))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_25 = QtWidgets.QLabel(self.frame_5)
        self.label_25.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame_5)
        self.label_26.setGeometry(QtCore.QRect(10, 30, 301, 91))
        self.label_26.setObjectName("label_26")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(420, 680, 181, 131))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_27 = QtWidgets.QLabel(self.frame_6)
        self.label_27.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame_6)
        self.label_28.setGeometry(QtCore.QRect(10, 30, 301, 91))
        self.label_28.setObjectName("label_28")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(710, 680, 171, 131))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_29 = QtWidgets.QLabel(self.frame_7)
        self.label_29.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame_7)
        self.label_30.setGeometry(QtCore.QRect(10, 30, 301, 91))
        self.label_30.setObjectName("label_30")
        self.label_8.raise_()
        self.label_3.raise_()
        self.frame.raise_()
        self.label_2.raise_()
        self.labelBemvindo.raise_()
        self.LineBuscar.raise_()
        self.label_7.raise_()
        self.labelFrase.raise_()
        self.nomeLogo.raise_()
        self.logo.raise_()
        self.botaoBuscar.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.botaoCesta.raise_()
        self.botaoEntrar.raise_()
        self.botaoCadastrar.raise_()
        self.frame_5.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelBemvindo.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.labelBemvindo.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#004b3f;\">BEM-VINDO À DROGALAUGH!</span></p></body></html>"))
        self.LineBuscar.setToolTip(_translate("MainWindow", "<html><head/><body><p><img src=\":/images/images/lupa.png\"/></p></body></html>"))
        self.LineBuscar.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><img src=\":/images/images/lupa.png\"/></p></body></html>"))
        self.LineBuscar.setPlaceholderText(_translate("MainWindow", "O que você está procurando?"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#004b3f;\">DESTAQUES DROGALAUGH</span></p></body></html>"))
        self.labelFrase.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Cuidando da sua saúde com dedicação!</span></p></body></html>"))
        self.nomeLogo.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.nomeLogo.setText(_translate("MainWindow", "DrogaLaugh"))
        self.botaoBuscar.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.BotaoReservar.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.BotaoReservar.setText(_translate("MainWindow", "Reserve seus produtos"))
        self.botaoOfertas.setText(_translate("MainWindow", "Visualize nossas ofertas"))
        self.botaoChat.setText(_translate("MainWindow", "Converse com nosso CHAT"))
        self.label_6.setText(_translate("MainWindow", "- 15%"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Vitamina C 1000mg</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">R$ 76.42 </span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>R$ 89.90</p></body></html>"))
        self.BotaoAddCesta.setText(_translate("MainWindow", "ADICIONAR"))
        self.label_11.setText(_translate("MainWindow", "- 15%"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Vitamina C 1000mg</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">R$ 76.42 </span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p>R$ 89.90</p></body></html>"))
        self.BotaoAddCesta_2.setText(_translate("MainWindow", "ADICIONAR"))
        self.label_15.setText(_translate("MainWindow", "- 15%"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Vitamina C 1000mg</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">R$ 76.42 </span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p>R$ 89.90</p></body></html>"))
        self.BotaoAddCesta_3.setText(_translate("MainWindow", "ADICIONAR"))
        self.label_20.setText(_translate("MainWindow", "- 15%"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Vitamina C 1000mg</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">R$ 76.42 </span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p>R$ 89.90</p></body></html>"))
        self.BotaoAddCesta_4.setText(_translate("MainWindow", "ADICIONAR"))
        self.botaoCesta.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.botaoCesta.setText(_translate("MainWindow", "R$0,00"))
        self.botaoEntrar.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.botaoEntrar.setText(_translate("MainWindow", "ENTRAR"))
        self.botaoCadastrar.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.botaoCadastrar.setText(_translate("MainWindow", "CADASTRAR"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Sobre Nós</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">A DrogaLaugh é sua farmácia de confiança, oferecendo</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> produtos de qualidade e atendimento excepcional </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">desde 2024.</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Contatos</span></p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">0800 123 4567</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">contato@drogalaugh.com</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Junco, 123</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Picos - PI</span></p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffffff;\">Redes Sociais</span></p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Instagram<br />Facebook</span></p></body></html>"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())