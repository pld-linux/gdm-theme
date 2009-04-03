# TODO:
#   - fix bogus (non-informative, English-in-pl) descriptions
#   - kill UTF where it shouldn't be (C descs are in us-ascii, pl in iso-8859-2,
#     Vendor in ???)
#
#
# This spec is generated from ./gdm-themes-spec-generator.sh script.
# You should find it in your `rpm --eval %_specdir`
# ??? -- I can't find any
#
Summary:	Themes for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motywy dla gdm (Zarządcy ekranów GNOME)
Name:		gdm-theme
Version:	2.6.0.6
Release:	3
License:	GPL
Group:		Themes
Source0:	http://art.gnome.org/download/themes/gdm_greeter/178/GDM-300-lantueno.tar.gz
# Source0-md5:	9fc35fec651a220abc0eb664e84cedd4
Source1:	http://art.gnome.org/download/themes/gdm_greeter/741/GDM-9nome-Darmis.tar.gz
# Source1-md5:	eb8bc9c85c2f2555959598cd2d53f1c1
Source2:	http://art.gnome.org/download/themes/gdm_greeter/89/GDM-Angel.tar.gz
# Source2-md5:	56c714da16420342d22659108055b647
Source4:	http://art.gnome.org/download/themes/gdm_greeter/509/GDM-BeeAtWork.tar.gz
# Source4-md5:	809566fd4f2cdc3e8d282b8328a8b2be
Source5:	http://art.gnome.org/download/themes/gdm_greeter/257/GDM-Bijou.tgz
# Source5-md5:	20fafc60a0a7f163d03c602e912f3660
Source6:	http://art.gnome.org/download/themes/gdm_greeter/90/GDM-Blueish.tar.gz
# Source6-md5:	b56faca3944bdc59e941b44197e89677
Source7:	http://art.gnome.org/download/themes/gdm_greeter/443/GDM-Butterfly.tar.gz
# Source7-md5:	821f9da7a5a6f00a682fd46481a0ad59
Source8:	http://art.gnome.org/download/themes/gdm_greeter/745/GDM-Windmill.tar.gz
# Source8-md5:	dcab44feec5b20084663f7a82026adba
Source9:	http://art.gnome.org/download/themes/gdm_greeter/91/GDM-Cracked-Windows.tar.gz
# Source9-md5:	4103efc6f74f54a83b172616167cb108
Source10:	http://art.gnome.org/download/themes/gdm_greeter/543/GDM-Cropcircles.tar.bz2
# Source10-md5:	7ea42e8a66188195d4b37d612c6b62d7
Source11:	http://art.gnome.org/download/themes/gdm_greeter/92/GDM-Crystal.tar.gz
# Source11-md5:	f89c4b0c29aec5d285ff2ce0199870a5
Source12:	http://art.gnome.org/download/themes/gdm_greeter/678/GDM-Crystal_for_Gnome.tar.gz
# Source12-md5:	e66965a9de2d669a41bf9499b3fbcb2b
Source13:	http://art.gnome.org/download/themes/gdm_greeter/720/GDM-CrystalforGnome2.tar.gz
# Source13-md5:	6face158fa1eafff50e753ba0758bc33
Source14:	http://art.gnome.org/download/themes/gdm_greeter/403/GDM-Crystal-Rose.tar.gz
# Source14-md5:	4ab12cbdb57c77320b0cf9790ce4daae
Source15:	http://art.gnome.org/download/themes/gdm_greeter/420/GDM-Cubic_Linux_Gnome.tar.gz
# Source15-md5:	95ed3fc14f07489a6bfad75db0b908f1
Source16:	http://art.gnome.org/download/themes/gdm_greeter/93/GDM-DartFrog.tar.bz2
# Source16-md5:	5ebb26d03f7eab3ac725ebb33c2becf6
Source17:	http://art.gnome.org/download/themes/gdm_greeter/184/GDM-Dawn.tar.gz
# Source17-md5:	5d81c298745480ca3d512a72429eb445
Source18:	http://art.gnome.org/download/themes/gdm_greeter/256/GDM-Daybreak.tar.gz
# Source18-md5:	238e80b7b1e4105cce13f381689ce761
Source19:	http://art.gnome.org/download/themes/gdm_greeter/449/GDM-Delicious.tar.gz
# Source19-md5:	1af671d07921b39278dd27cff8ea4247
Source20:	http://art.gnome.org/download/themes/gdm_greeter/404/GDM-DevilsCandy.tar.gz
# Source20-md5:	60c44dd459386f60bffa1698bedca9e2
Source21:	http://art.gnome.org/download/themes/gdm_greeter/459/GDM-Dreaming-Alien.tar.gz
# Source21-md5:	a9d8e1dc49408e32571fc4985cfbb4f3
Source22:	http://art.gnome.org/download/themes/gdm_greeter/96/GDM-DumbCloud.tar.gz
# Source22-md5:	8da61b45e88602adcad82c8b92869604
Source23:	http://art.gnome.org/download/themes/gdm_greeter/98/GDM-Emo-Blue.tar.gz
# Source23-md5:	5dcbf93484203a9e594264878a8e7699
Source24:	http://art.gnome.org/download/themes/gdm_greeter/310/GDM-Falling-Angel.tar.gz
# Source24-md5:	95c2d2f79cb72a47d26b373e603ed250
Source25:	http://art.gnome.org/download/themes/gdm_greeter/223/GDM-Flame.tar.gz
# Source25-md5:	82219dd6ec558efbf0fb81ce4b27eb4c
Source26:	http://art.gnome.org/download/themes/gdm_greeter/99/GDM-Flowers.tar.gz
# Source26-md5:	7763649e7acca699bb25df0fc6e1c079
Source27:	http://art.gnome.org/download/themes/gdm_greeter/460/GDM-gcr-ddlm.tar.gz
# Source27-md5:	91ebc74754d87bf8f6def76bbe8e5844
Source28:	http://art.gnome.org/download/themes/gdm_greeter/508/GDM-Dropline.tar.gz
# Source28-md5:	4ce8fd37e8bb56183ff78c40dcaad7f6
Source29:	http://art.gnome.org/download/themes/gdm_greeter/775/GDM-Waves.tar.bz2
# Source29-md5:	3a010b89e7ea84ccad0e6825d9e41e0b
Source30:	http://art.gnome.org/download/themes/gdm_greeter/196/GDM-GlassFoot.tar.gz
# Source30-md5:	5220133ad1b367500b559d57cc1eb02f
Source31:	http://art.gnome.org/download/themes/gdm_greeter/361/GDM-Mosaic.tar.gz
# Source31-md5:	a4673c14f17fb129f07348b4bd2a9382
Source32:	http://art.gnome.org/download/themes/gdm_greeter/298/GDM-Glassy.tar.gz
# Source32-md5:	b4db73c515b95cec7c72514b53d96413
Source33:	http://art.gnome.org/download/themes/gdm_greeter/294/GDM-Chilie.tar.gz
# Source33-md5:	a115430ff4925efd65047de7e81e31c8
Source34:	http://art.gnome.org/download/themes/gdm_greeter/772/GDM-PlainSwoosh.tar.gz
# Source34-md5:	8ff96716b4e5222335322ebbdb176e93
Source35:	http://art.gnome.org/download/themes/gdm_greeter/773/GDM-PlainSwooshTng.tar.gz
# Source35-md5:	dba0deeea42346b43c563670d92b3b58
Source36:	http://art.gnome.org/download/themes/gdm_greeter/311/GDM-Hantzley.tar.gz
# Source36-md5:	3e1678c28a82e6ac814d0f250d71a727
Source37:	http://art.gnome.org/download/themes/gdm_greeter/33/GDM-Hunter.tar.gz
# Source37-md5:	50abd5fbb23e22914a6654d4903a6833
Source38:	http://art.gnome.org/download/themes/gdm_greeter/240/GDM-Hybridfusion.tar.gz
# Source38-md5:	9397e525790f0232ec9f45d48649f07e
Source39:	http://art.gnome.org/download/themes/gdm_greeter/742/GDM-InThisWorld.tar.bz2
# Source39-md5:	e6b532e502f49e79af730d415af9a1a1
Source40:	http://art.gnome.org/download/themes/gdm_greeter/396/GDM-KDE-Crystal.tar.gz
# Source40-md5:	3bd019cf594a6ef78a5dab0bc9b8023f
Source41:	http://art.gnome.org/download/themes/gdm_greeter/527/GDM-Kinkakuji.tar.gz
# Source41-md5:	d35e28892c37a5c445bccb3c8f30de60
Source42:	http://art.gnome.org/download/themes/gdm_greeter/278/GDM-Knoke.tar.gz
# Source42-md5:	32378f58ab198dbe4bd2ad9709ac8bf6
Source43:	http://art.gnome.org/download/themes/gdm_greeter/303/GDM-labisbal.tar.gz
# Source43-md5:	dd6b2d7d8fd40a82adab35707b828eab
Source44:	http://art.gnome.org/download/themes/gdm_greeter/244/GDM-Leon.tar.gz
# Source44-md5:	ea73242c8f54aaf9650453cefbc9b897
Source45:	http://art.gnome.org/download/themes/gdm_greeter/588/GDM-Linux_Crystal.tar.gz
# Source45-md5:	640c12b3f044f134fea53635b9bc21f2
Source46:	http://art.gnome.org/download/themes/gdm_greeter/511/GDM-LinuxTux.tar.gz
# Source46-md5:	2334031099d73c3afe2d4a05633a6634
Source47:	http://art.gnome.org/download/themes/gdm_greeter/774/GDM-IndlinuxLuna.tar
# Source47-md5:	516f8d465ca6b25d24f370674f3d326d
Source48:	http://art.gnome.org/download/themes/gdm_greeter/743/GDM-M83.tar.gz
# Source48-md5:	201726bc6f1eb7b640d180d6692e9034
Source49:	http://art.gnome.org/download/themes/gdm_greeter/300/GDM-MachuPicchu.tar.gz
# Source49-md5:	fd876d92468e4881ec8213e69e79ec9f
Source50:	http://art.gnome.org/download/themes/gdm_greeter/747/GDM-ManzanaTux.tar.gz
# Source50-md5:	d725cb1afc0b8635215029d7d46946b9
Source51:	http://art.gnome.org/download/themes/gdm_greeter/748/GDM-ManzanaTuxBlack.tar.gz
# Source51-md5:	3049cd183d4a93b8ccf4ba61f8f47bea
Source52:	http://art.gnome.org/download/themes/gdm_greeter/533/GDM-Milk.tar.gz
# Source52-md5:	faf11a2f6e7ff36a822bd553b6cdbe21
Source53:	http://art.gnome.org/download/themes/gdm_greeter/448/GDM-Mirrored-0.8.tar.gz
# Source53-md5:	97f308b23e5643fc14e9817168796879
Source54:	http://art.gnome.org/download/themes/gdm_greeter/494/GDM-MonoMetal.tar.gz
# Source54-md5:	178fb25cfc57997e63cecc5279e7a0dd
Source55:	http://art.gnome.org/download/themes/gdm_greeter/103/GDM-Morning.tar.bz2
# Source55-md5:	b6ffafe1d608d4f345c3c6fac0cba29f
Source56:	http://art.gnome.org/download/themes/gdm_greeter/325/GDM-Mozi.tar.gz
# Source56-md5:	0ea48d8805189567a92fe987b959bacd
Source57:	http://art.gnome.org/download/themes/gdm_greeter/243/GDM-Murcia.tgz
# Source57-md5:	057d34a3435af7dbdc9637d2c2ec3dc7
Source58:	http://art.gnome.org/download/themes/gdm_greeter/270/GDM-OpenSource.tgz
# Source58-md5:	1845e772f6b5ca0bcfdfacb5b68f9d1f
Source59:	http://art.gnome.org/download/themes/gdm_greeter/272/GDM-penguin.tar.gz
# Source59-md5:	19de4049ad36693e9c9aafe373c2c7ca
Source60:	http://art.gnome.org/download/themes/gdm_greeter/754/GDM-PeppeForGnome.tar.gz
# Source60-md5:	60c9c484c619cb90f44ebd5e5430b58a
Source61:	http://art.gnome.org/download/themes/gdm_greeter/463/GDM-pixelgdm.tar.gz
# Source61-md5:	218d02a637ee040450fd6f08039011de
Source62:	http://art.gnome.org/download/themes/gdm_greeter/464/GDM-Red-Leaves.tar.gz
# Source62-md5:	f2c0b9aa3638dbfef408a1d4a270eaaa
Source63:	http://art.gnome.org/download/themes/gdm_greeter/301/GDM-RV.tar.gz
# Source63-md5:	929027123d47db1a4e5f8cd41493739a
Source64:	http://art.gnome.org/download/themes/gdm_greeter/107/GDM-Sea.tar.gz
# Source64-md5:	0a200b93f8081df5d3c779281c6b2bfc
Source65:	http://art.gnome.org/download/themes/gdm_greeter/111/GDM-Segovia.tar.gz
# Source65-md5:	ce5a826adad38d70bd42bb2a21a87074
Source66:	http://art.gnome.org/download/themes/gdm_greeter/108/GDM-Segovia-Night.tar.gz
# Source66-md5:	a85f01841618f29e9f01a307e77041dd
Source67:	http://art.gnome.org/download/themes/gdm_greeter/776/GDM-Shapy.tar.gz
# Source67-md5:	fa692e75cfe9a6d506af42d2bb418bc2
Source68:	http://art.gnome.org/download/themes/gdm_greeter/617/GDM-Simple-Gnome-Logo.tar.gz
# Source68-md5:	a637179b837a4dfd13f6068075f5ec0a
Source69:	http://art.gnome.org/download/themes/gdm_greeter/222/GDM-Space.tar.gz
# Source69-md5:	37f97143298be0f7822258f643b72d0c
Source71:	http://art.gnome.org/download/themes/gdm_greeter/744/GDM-SpreadFirefox.tar.gz
# Source71-md5:	ba5ab37111d17f96a1f57d3dda157d42
Source72:	http://art.gnome.org/download/themes/gdm_greeter/109/GDM-STGO.tar.gz
# Source72-md5:	7961582f7bfc80accc7c3a9a6c1c42a8
Source73:	http://art.gnome.org/download/themes/gdm_greeter/267/GDM-Tcpa.tar.gz
# Source73-md5:	144240a042baff4af3e0fd1a2a509f1a
Source74:	http://art.gnome.org/download/themes/gdm_greeter/746/GDM-Sakura.tar.gz
# Source74-md5:	74f3582953db9fcc971b8465f5042ed4
Source75:	http://art.gnome.org/download/themes/gdm_greeter/419/GDM-Synergy.tar.gz
# Source75-md5:	a0cb7549b2507eb9fac2995996f0bc53
Source76:	http://art.gnome.org/download/themes/gdm_greeter/525/GDM-Taipei.tar.gz
# Source76-md5:	20c3d22c3622bf5f2fc1f3e771913145
Source77:	http://art.gnome.org/download/themes/gdm_greeter/293/GDM-Darkcrystal.tar.bz2
# Source77-md5:	d6d8c3cab9c1790db3bcd05596f4cf75
Source78:	http://art.gnome.org/download/themes/gdm_greeter/332/GDM-Todmorden.tar.gz
# Source78-md5:	c6222e888f43c83243a61083d5afb324
Source79:	http://art.gnome.org/download/themes/gdm_greeter/242/GDM-Valladolid.tar.gz
# Source79-md5:	1530c57898443bc3336cc4612a572055
Source80:	http://art.gnome.org/download/themes/gdm_greeter/182/GDM-xpto.tar.gz
# Source80-md5:	adcdc03f36d9a9c72d64a77ba98f5045
URL:		http://art.gnome.org/
Requires:	gdm
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows you to change the look of your GNOME Display
Manager :-)

%description -l pl.UTF-8
Ten pakiet pozwala na zmiane wyglądu Zarządcy ekranów GNOME :-)

%package 300-lantueno
Summary:	Theme 300-lantueno for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw 300-lantueno dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Naciu
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/178/
Requires:	%{name}

%description 300-lantueno
Theme '300-lantueno' by 'I Wayan Suryadarma'. Author's comment for the
theme: Theme based on Lantueno; year 1911 (Cantabria, Spain).

%description 300-lantueno -l pl.UTF-8
Motyw '300-lantueno' autorstwa 'I Wayan Suryadarma'. Komentarz autora
do motywu: Theme based on Lantueno; year 1911 (Cantabria, Spain).

%package 9nome-Darmis
Summary:	Theme 9nome-Darmis for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw 9nome-Darmis dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		I Wayan Suryadarma
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/178/
Requires:	%{name}

%description 9nome-Darmis
Theme '9nome-Darmis' by 'I Wayan Suryadarma'. Author's comment for the
theme: This is my first GDM and I like it.

%description 9nome-Darmis -l pl.UTF-8
Motyw '9nome-Darmis' autorstwa 'I Wayan Suryadarma'. Komentarz autora
do motywu: This is my first GDM and I like it.

%package Angel
Summary:	Theme Angel for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Angel dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Bert De Meyer
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/89/
Requires:	%{name}

%description Angel
Theme 'Angel' by 'Bert De Meyer'. Author's comment for the theme:
Note: This themes is based on an old Windowmaker theme from Largo that
you can still find at: <http://largo.windowmaker.org/themes/>.

%description Angel -l pl.UTF-8
Motyw 'Angel' autorstwa 'Bert De Meyer'. Komentarz autora do motywu:
Note: This themes is based on an old Windowmaker theme from Largo that
you can still find at: <http://largo.windowmaker.org/themes/>.

%package Barcelona
Summary:	Theme Barcelona for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Barcelona dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Alvaro del Castillo
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/241/
Requires:	%{name}

%description Barcelona
Theme 'Barcelona' by 'Alvaro del Castillo'.

%description Barcelona -l pl.UTF-8
Motyw 'Barcelona' autorstwa 'Ălvaro del Castillo'.

%package Bee_at_Work
Summary:	Theme Bee_at_Work for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Bee_at_Work dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Julian Coccia
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/509/
Requires:	%{name}

%description Bee_at_Work
Theme 'Bee_at_Work' by 'Julian Coccia'. Author's comment for the
theme: A nice GDM greeter theme in black and yellow, based on one of
my pictures.

%description Bee_at_Work -l pl.UTF-8
Motyw 'Bee_at_Work' autorstwa 'Julian Coccia'. Komentarz autora do
motywu: A nice GDM greeter theme in black and yellow, based on one of
my pictures.

%package Bijou
Summary:	Theme Bijou for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Bijou dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Alex Fraser
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/257/
Requires:	%{name}

%description Bijou
Theme 'Bijou' by 'Alex Fraser'. Author's comment for the theme: Simple
and clean with highly polished buttons

%description Bijou -l pl.UTF-8
Motyw 'Bijou' autorstwa 'Alex Fraser'. Komentarz autora do motywu:
Simple and clean with highly polished buttons

%package Blueish
Summary:	Theme Blueish for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Blueish dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Michael Thomas, Henrik Brix Andersen
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/90/
Requires:	%{name}

%description Blueish
Theme 'Blueish' by 'Michael Thomas, Henrik Brix Andersen'. Authors'
comment for the theme: A metallic GNOME foot on a blue background.
Credits for the background goes to Henrik Brix Andersen.

%description Blueish -l pl.UTF-8
Motyw 'Blueish' autorstwa 'Michael Thomas, Henrik Brix Andersen'.
Komentarz autorów do motywu: A metallic GNOME foot on a blue
background. Credits for the background goes to Henrik Brix Andersen.

%package Butterfly
Summary:	Theme Butterfly for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Butterfly dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		sgaap
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/443/
Requires:	%{name}

%description Butterfly
Theme 'Butterfly' by 'sgaap'. Author's comment for the theme: A bright
theme :)

%description Butterfly -l pl.UTF-8
Motyw 'Butterfly' autorstwa 'sgaap'. Komentarz autora do motywu: A
bright theme :)

%package Colorado_Windmill
Summary:	Theme Colorado_Windmill for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Colorado_Windmill dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Scott W. Taylor
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/745/
Requires:	%{name}

%description Colorado_Windmill
Theme 'Colorado_Windmill' by 'Scott W. Taylor'. Author's comment for
the theme: Windmill in the grasslands of Colorado.

%description Colorado_Windmill -l pl.UTF-8
Motyw 'Colorado_Windmill' autorstwa 'Scott W. Taylor'. Komentarz
autora do motywu: Windmill in the grasslands of Colorado.

%package Cracked_Windows
Summary:	Theme Cracked_Windows for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Cracked_Windows dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Ovidiu Cernautan
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/91/
Requires:	%{name}

%description Cracked_Windows
Theme 'Cracked_Windows' by 'Ovidiu Cernautan'. Author's comment for
the theme: It's pretty colorful but I like it and I hope you'll like
it too.

%description Cracked_Windows -l pl.UTF-8
Motyw 'Cracked_Windows' autorstwa 'Ovidiu Cernautan'. Komentarz autora
do motywu: It's pretty colorful but I like it and I hope you'll like
it too.

%package Crop_Circles
Summary:	Theme Crop_Circles for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Crop_Circles dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Will Reinhart
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/543/
Requires:	%{name}

%description Crop_Circles
Theme 'Crop_Circles' by 'Will Reinhart'. Author's comment for the
theme: Signs of intelligent life! This is graphical face-browser
theme, so it requires GDM from Gnome 2.4.0. Thanks to Jiin Yaroon for
the wallpaper this theme's background is based on.

%description Crop_Circles -l pl.UTF-8
Motyw 'Crop_Circles' autorstwa 'Will Reinhart'. Komentarz autora do
motywu: Signs of intelligent life! This is graphical face-browser
theme, so it requires GDM from Gnome 2.4.0. Thanks to Jiin Yaroon for
the wallpaper this theme's background is based on.

%package Crystal
Summary:	Theme Crystal for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Crystal dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Niek van der Maas
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/92/
Requires:	%{name}

%description Crystal
Theme 'Crystal' by 'Niek van der Maas'. Author's comment for the
theme: Crystal Theme for GDM by Niek van der Maas. All images were
made by Everaldo.

%description Crystal -l pl.UTF-8
Motyw 'Crystal' autorstwa 'Niek van der Maas'. Komentarz autora do
motywu: Crystal Theme for GDM by Niek van der Maas. All images were
made by Everaldo.

%package Crystal_For_Gnome
Summary:	Theme Crystal_For_GNOME for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Crystal_For_GNOME dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Keifer
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/678/
Requires:	%{name}

%description Crystal_For_Gnome
Theme 'Crystal_For_Gnome' by 'Keifer'. Author's comment for the theme:
A crystal gdm theme that includes a wallpaper by Chromakode, and icons
by Everaldo. Must have a version of gdm that is compatable with
facethemes to function.

%description Crystal_For_Gnome -l pl.UTF-8
Motyw 'Crystal_For_Gnome' autorstwa 'Keifer'. Komentarz autora do
motywu: A crystal gdm theme that includes a wallpaper by Chromakode,
and icons by Everaldo. Must have a version of gdm that is compatable
with facethemes to function.

%package Crystal_for_Gnome_-_theme_2
Summary:	Theme Crystal_for_GNOME_-_theme_2 for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Crystal_for_GNOME_-_theme_2 dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Keifer Miller
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/720/
Requires:	%{name}

%description Crystal_for_Gnome_-_theme_2
Theme 'Crystal_for_Gnome_-_theme_2' by 'Keifer Miller'. Author's
comment for the theme: Created by member Keifer of the Crystal for
Gnome project.

%description Crystal_for_Gnome_-_theme_2 -l pl.UTF-8
Motyw 'Crystal_for_Gnome_-_theme_2' autorstwa 'Keifer Miller'.
Komentarz autora do motywu: Created by member Keifer of the Crystal
for Gnome project.

%package Crystal_Rose
Summary:	Theme Crystal_Rose for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Crystal_Rose dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Carlos (StackGuard) Ferreira
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/403/
Requires:	%{name}

%description Crystal_Rose
Theme 'Crystal_Rose' by 'Carlos (StackGuard) Ferreira'. Author's
comment for the theme: Blue and shadded theme I've made for my
girlfriend, based on a wallpaper found in deviantart.com .

%description Crystal_Rose -l pl.UTF-8
Motyw 'Crystal_Rose' autorstwa 'Carlos (StackGuard) Ferreira'.
Komentarz autora do motywu: Blue and shadded theme I've made for my
girfriend, based on a wallpaper found in deviantart.com .

%package Cubic_Linux_and_Gnome
Summary:	Theme Cubic_Linux_and_GNOME for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Cubic_Linux_and_GNOME dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		jam
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/420/
Requires:	%{name}

%description Cubic_Linux_and_Gnome
Theme 'Cubic_Linux_and_Gnome' by 'jam'. Author's comment for the
theme: Background is render of a cube showing 2 faces. Tux on 1 face,
Gnome logo on the other.

%description Cubic_Linux_and_Gnome -l pl.UTF-8
Motyw 'Cubic_Linux_and_Gnome' autorstwa 'jam'. Komentarz autora do
motywu: Background is render of a cube showing 2 faces. Tux on 1 face,
Gnome logo on the other.

%package Dart_Frog
Summary:	Theme Dart_Frog for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Dart_Frog dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Wreckd
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/93/
Requires:	%{name}

%description Dart_Frog
Theme 'Dart_Frog' by 'Wreckd'. Author's comment for the theme: Nice
little theme with a background I found. So, can anyone tell me what
kinda frog this is?

%description Dart_Frog -l pl.UTF-8
Motyw 'Dart_Frog' autorstwa 'Wreckd'. Komentarz autora do motywu: Nice
little theme with a background I found. So, can anyone tell me what
kinda frog this is?

%package Dawn
Summary:	Theme Dawn for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Dawn dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Gianluca Masci
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/184/
Requires:	%{name}

%description Dawn
Theme 'Dawn' by 'Gianluca Masci'. Author's comment for the theme: Dawn
in mountain.

%description Dawn -l pl.UTF-8
Motyw 'Dawn' autorstwa 'Gianluca Masci'. Komentarz autora do motywu:
Dawn in mountain.

%package Daybreak
Summary:	Theme Daybreak for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Daybreak dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Francis Tyers
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/256/
Requires:	%{name}

%description Daybreak
Theme 'Daybreak' by 'Francis Tyers'. Author's comment for the theme:
Found a cool background on deviantart.com and set myself up the gdm
theme.

%description Daybreak -l pl.UTF-8
Motyw 'Daybreak' autorstwa 'Francis Tyers'. Komentarz autora do
motywu: Found a cool background on deviantart.com and set myself up
the gdm theme.

%package Delicious
Summary:	Theme Delicious for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Delicious dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Roman Joost
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/449/
Requires:	%{name}

%description Delicious
Theme 'Delicious' by 'Roman Joost'. Author's comment for the theme:
Delicious is a comic theme that uses clean icons and a funny
background.

%description Delicious -l pl.UTF-8
Motyw 'Delicious' autorstwa 'Roman Joost'. Komentarz autora do motywu:
Delicious is a comic theme that uses clean icons and a funny
background.

%package Devils_Candy
Summary:	Theme Devils_Candy for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Devils_Candy dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Slayer[nFc]
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/404/
Requires:	%{name}

%description Devils_Candy
Theme 'Devils_Candy' by 'Slayer[nFc]'. Author's comment for the theme:
My first GDM theme based on DevilsCandy by Xebra 2001.

%description Devils_Candy -l pl.UTF-8
Motyw 'Devils_Candy' autorstwa 'Slayer[nFc]'. Komentarz autora do
motywu: My first GDM theme based on DevilsCandy by Xebra 2001.

%package Dreaming_Alien
Summary:	Theme Dreaming_Alien for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Dreaming_Alien dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Christopher V. Browne
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/459/
Requires:	%{name}

%description Dreaming_Alien
Theme 'Dreaming_Alien' by 'Christopher V. Browne'. Author's comment
for the theme: Renoiro's Dreaming Alien - artist approved Buttons
borrow from Bijou.

%description Dreaming_Alien -l pl.UTF-8
Motyw 'Dreaming_Alien' autorstwa 'Christopher V. Browne'. Komentarz
autora do motywu: Renoiro's Dreaming Alien - artist approved Buttons
borrow from Bijou.

%package DumbCloud
Summary:	Theme DumbCloud for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw DumbCloud dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Unknown
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/96/
Requires:	%{name}

%description DumbCloud
Theme 'DumbCloud' by 'Unknown'. Author's comment for the theme: Dunno
if this is 'legal', I'm not an artist or technically inclined but I
took the photo of the cloud & made the image of lines & borrowed the
other graphics from the default Circles GDM greeter theme. I'm don't
know XML & don't want to learn it, so I only changed the filenames to
display my own. This is my attempt, it's worse than the default one
but I just wanted to try it & have something different. For real
artists, just edit the files in /usr/share/gdm/themes - if I could do
it, you can.

%description DumbCloud -l pl.UTF-8
Motyw 'DumbCloud' autorstwa 'Unknown'. Komentarz autora do motywu:
Dunno if this is 'legal', I'm not an artist or technically inclined
but I took the photo of the cloud & made the image of lines & borrowed
the other graphics from the default Circles GDM greeter theme. I'm
don't know XML & don't want to learn it, so I only changed the
filenames to display my own. This is my attempt, it's worse than the
default one but I just wanted to try it & have something different.
For real artists, just edit the files in /usr/share/gdm/themes - if I
could do it, you can.

%package Emo-Blue
Summary:	Theme Emo-Blue for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Emo-Blue dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Paul Hendrick
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/98/
Requires:	%{name}

%description Emo-Blue
Theme 'Emo-Blue' by 'Paul Hendrick'. Author's comment for the theme: A
theme using a cool futuristic background and nice GNOME2 icons.

%description Emo-Blue -l pl.UTF-8
Motyw 'Emo-Blue' autorstwa 'Paul Hendrick'. Komentarz autora do
motywu: A theme using a cool futuristic background and nice GNOME2
icons.

%package Falling_Angel
Summary:	Theme Falling_Angel for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Falling_Angel dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Carlos (StackGuard) Ferreira
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/310/
Requires:	%{name}

%description Falling_Angel
Theme 'Falling_Angel' by 'Carlos (StackGuard) Ferreira'. Author's
comment for the theme: An atempt to make a GDM Greeter theme, based on
a beautiful wallpaper :)

%description Falling_Angel -l pl.UTF-8
Motyw 'Falling_Angel' autorstwa 'Carlos (StackGuard) Ferreira'.
Komentarz autora do motywu: An atempt to make a GDM Greeter theme,
based on a beautiful wallpaper :)

%package Fire_Breathing_Robot
Summary:	Theme Fire_Breathing_Robot for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Fire_Breathing_Robot dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		John Cantrell
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/223/
Requires:	%{name}

%description Fire_Breathing_Robot
Theme 'Fire_Breathing_Robot' by 'John Cantrell'. Author's comment for
the theme: A neat little fire breathing robot for your login. Based
off the Redhat's bluecurve.

%description Fire_Breathing_Robot -l pl.UTF-8
Motyw 'Fire_Breathing_Robot' autorstwa 'John Cantrell'. Komentarz
autora do motywu: A neat little fire breathing robot for your login.
Based off the Redhat's bluecurve.

%package Flowers
Summary:	Theme Flowers for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Flowers dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Gianluca Masci
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/99/
Requires:	%{name}

%description Flowers
Theme 'Flowers' by 'Gianluca Masci'. Author's comment for the theme: A
Theme with Flowers.

%description Flowers -l pl.UTF-8
Motyw 'Flowers' autorstwa 'Gianluca Masci'. Komentarz autora do
motywu: A Theme with Flowers.

%package gcr-ddlm
Summary:	Theme gcr-ddlm for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw gcr-ddlm dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		ghost_crab
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/460/
Requires:	%{name}

%description gcr-ddlm
Theme 'gcr-ddlm' by 'ghost_crab'. Author's comment for the theme: dia
de los muertos GDM theme. My first. Please let me know what I need to
do to fix it. Rock!

%description gcr-ddlm -l pl.UTF-8
Motyw 'gcr-ddlm' autorstwa 'ghost_crab'. Komentarz autora do motywu:
dia de los muertos GDM theme. My first. Please let me know what I need
to do to fix it. Rock!

%package Gdm_Dropline
Summary:	Theme Gdm_Dropline for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Gdm_Dropline dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		elmaya
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/508/
Requires:	%{name}

%description Gdm_Dropline
Theme 'Gdm_Dropline' by 'elmaya'. Author's comment for the theme: A
GDM theme to go with the dropline splash screen.

%description Gdm_Dropline -l pl.UTF-8
Motyw 'Gdm_Dropline' autorstwa 'elmaya'. Komentarz autora do motywu: A
GDM theme to go with the dropline splash screen.

%package GDM_Waves
Summary:	Theme GDM_Waves for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw GDM_Waves dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Marco
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/775/
Requires:	%{name}

%description GDM_Waves
Theme 'GDM_Waves' by 'Marco'. Author's comment for the theme: my first
GDM theme.

%description GDM_Waves -l pl.UTF-8
Motyw 'GDM_Waves' autorstwa 'Marco'. Komentarz autora do motywu: my
first GDM theme.

%package GDM-GlassFoot
Summary:	Theme GDM-GlassFoot for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw GDM-GlassFoot dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Burcin Donmez
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/196/
Requires:	%{name}

%description GDM-GlassFoot
Theme 'GDM-GlassFoot' by 'Burcin Donmez'. Author's comment for the
theme: GDM greeter using GNOME-GlassFoot background image from
Waldgeist.

%description GDM-GlassFoot -l pl.UTF-8
Motyw 'GDM-GlassFoot' autorstwa 'Burcin Donmez'. Komentarz autora do
motywu: GDM greeter using GNOME-GlassFoot background image from
Waldgeist.

%package GDM-Mosaic
Summary:	Theme GDM-Mosaic for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw GDM-Mosaic dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		soho501
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/361/
Requires:	%{name}

%description GDM-Mosaic
Theme 'GDM-Mosaic' by 'soho501'. Author's comment for the theme:
That's the bull's shadow mosaic...

%description GDM-Mosaic -l pl.UTF-8
Motyw 'GDM-Mosaic' autorstwa 'soho501'. Komentarz autora do motywu:
That's the bull's shadow mosaic...

%package Glassy
Summary:	Theme Glassy for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Glassy dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Christopher A. Shamis
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/298/
Requires:	%{name}

%description Glassy
Theme 'Glassy' by 'Christopher A. Shamis'. Author's comment for the
theme: Ray-traced glass cork-screw over a shiny checkered floor.

%description Glassy -l pl.UTF-8
Motyw 'Glassy' autorstwa 'Christopher A. Shamis'. Komentarz autora do
motywu: Ray-traced glass cork-screw over a shiny checkered floor.

%package Gnome_Chile
Summary:	Theme GNOME_Chile for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw GNOME_Chile dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Andrés "Death_Knight" Villagrán
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/294/
Requires:	%{name}

%description Gnome_Chile
Theme 'Gnome_Chile' by 'Andrés "Death_Knight" Villagrán'. Author's
comment for the theme: EN: It's a best Theme of GNOME in Chile ES:
Este tema es exelente, bonito y muy atrallente MADE IN CHILE.

%description Gnome_Chile -l pl.UTF-8
Motyw 'Gnome_Chile' autorstwa 'AndrĂŠs "Death_Knight" VillagrĂĄn'.
Komentarz autora do motywu: EN: It's a best Theme of GNOME in Chile
ES: Este tema es exelente, bonito y muy atrallente MADE IN CHILE.

%package Gnome_Plain_Swoosh_GDM_Theme
Summary:	Theme GNOME_Plain_Swoosh_GDM_Theme for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw GNOME_Plain_Swoosh_GDM_Theme dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Michael Flaig
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/772/
Requires:	%{name}

%description Gnome_Plain_Swoosh_GDM_Theme
Theme 'Gnome_Plain_Swoosh_GDM_Theme' by 'Michael Flaig'. Author's
comment for the theme: This theme features "Gnome Plain Swoosh" (an
1600x1200 Wallpaper) which I found on art.gnome.org... I hope you like
it Wallpaper "Gnome Plain Swoosh" by: Morgan Collins Based on: Onebase
GDM Theme by P.Yavitz.

%description Gnome_Plain_Swoosh_GDM_Theme -l pl.UTF-8
Motyw 'Gnome_Plain_Swoosh_GDM_Theme' autorstwa 'Michael Flaig'.
Komentarz autora do motywu: This theme features "Gnome Plain Swoosh"
(an 1600x1200 Wallpaper) which I found on art.gnome.org... I hope you
like it Wallpaper "Gnome Plain Swoosh" by: Morgan Collins Based on:
Onebase GDM Theme by P.Yavitz.

%package Gnome_Plain_Swoosh_GDM_Theme_TNG
Summary:	Theme GNOME_Plain_Swoosh_GDM_Theme_TNG for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw GNOME_Plain_Swoosh_GDM_Theme_TNG dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Michael Flaig
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/773/
Requires:	%{name}

%description Gnome_Plain_Swoosh_GDM_Theme_TNG
Theme 'Gnome_Plain_Swoosh_GDM_Theme_TNG' by 'Michael Flaig'. Author's
comment for the theme: This theme features "Gnome Plain Swoosh" (an
1600x1200 Wallpaper) and the Novell Linux Desktop GDM Theme. Theme by:
Michael Flaig Based on: Novel Linux Desktop GDM Theme by Tigert
Wallpaper "Gnome Plain Swoosh" by: Morgan Collins.

%description Gnome_Plain_Swoosh_GDM_Theme_TNG -l pl.UTF-8
Motyw 'Gnome_Plain_Swoosh_GDM_Theme_TNG' autorstwa 'Michael Flaig'.
Komentarz autora do motywu: This theme features "Gnome Plain Swoosh"
(an 1600x1200 Wallpaper) and the Novell Linux Desktop GDM Theme. Theme
by: Michael Flaig Based on: Novel Linux Desktop GDM Theme by Tigert
Wallpaper "Gnome Plain Swoosh" by: Morgan Collins.

%package Hantzley
Summary:	Theme Hantzley for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Hantzley dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Hantzley
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/311/
Requires:	%{name}

%description Hantzley
Theme 'Hantzley' by 'Hantzley'. Author's comment for the theme: My
first GDM Greeter Theme. Hope you like it.

%description Hantzley -l pl.UTF-8
Motyw 'Hantzley' autorstwa 'Hantzley'. Komentarz autora do motywu: My
first GDM Greeter Theme. Hope you like it.

%package Hunter
Summary:	Theme Hunter for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Hunter dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Michael Thomas
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/33/
Requires:	%{name}

%description Hunter
Theme 'Hunter' by 'Michael Thomas'. Author's comment for the theme:
Circles theme that uses a image instead of a SVG file.

%description Hunter -l pl.UTF-8
Motyw 'Hunter' autorstwa 'Michael Thomas'. Komentarz autora do motywu:
Circles theme that uses a image instead of a svg file.

%package hybridFUSION
Summary:	Theme hybridFUSION for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw hybridFUSION dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Vincent Mac
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/240/
Requires:	%{name}

%description hybridFUSION
Theme 'hybridFUSION' by 'Vincent Mac'. Author's comment for the theme:
hybridFUSION is a theme based on Night Elf with some different
artwork.

%description hybridFUSION -l pl.UTF-8
Motyw 'hybridFUSION' autorstwa 'Vincent Mac'. Komentarz autora do
motywu: hybridFUSION is a theme based on Night Elf with some different
artwork.

%package In_This_World
Summary:	Theme In_This_World for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw In_This_World dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Job Diogenes Ribeiro Borges
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/742/
Requires:	%{name}

%description In_This_World
Theme 'In_This_World' by 'Job Diogenes Ribeiro Borges'. Author's
comment for the theme: Theme based on the background In This World
from Vlad Gerasimov <http://www.vladstudio.com/>.

%description In_This_World -l pl.UTF-8
Motyw 'In_This_World' autorstwa 'Job Diogenes Ribeiro Borges'.
Komentarz autora do motywu: Theme based on the background In This
World from Vlad Gerasimov <http://www.vladstudio.com/>.

%package KDE_Crystal
Summary:	Theme KDE_Crystal for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw KDE_Crystal dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Yann Bouan
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/396/
Requires:	%{name}

%description KDE_Crystal
Theme 'KDE_Crystal' by 'Yann Bouan'. Author's comment for the theme: A
theme inspired by the KDE crystal icon theme.

%description KDE_Crystal -l pl.UTF-8
Motyw 'KDE_Crystal' autorstwa 'Yann Bouan'. Komentarz autora do
motywu: A theme inspired by the KDE crystal icon theme.

%package Kinkakuji
Summary:	Theme Kinkakuji for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Kinkakuji dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Cholwich Nattee
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/527/
Requires:	%{name}

%description Kinkakuji
Theme 'Kinkakuji' by 'Cholwich Nattee'. Author's comment for the
theme: Kinkakuji (The temple of the Golden Pavilion) in Kyoto Japan.

%description Kinkakuji -l pl.UTF-8
Motyw 'Kinkakuji' autorstwa 'Cholwich Nattee'. Komentarz autora do
motywu: Kinkakuji (The temple of the Golden Pavilion) in Kyoto Japan.

%package Knoke
Summary:	Theme Knoke for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Knoke dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Dietrich Heise
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/278/
Requires:	%{name}

%description Knoke
Theme 'Knoke' by 'Dietrich Heise'. Author's comment for the theme: A
GDM Greeter Theme with my cat 'Knoke'.

%description Knoke -l pl.UTF-8
Motyw 'Knoke' autorstwa 'Dietrich Heise'. Komentarz autora do motywu:
A GDM Greeter Theme with my cat 'Knoke'.

%package La_Bisbal_dEmpord_nevada
Summary:	Theme La_Bisbal_dEmpord_nevada for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw La_Bisbal_dEmpord_nevada dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Radio Bisbal
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/303/
Requires:	%{name}

%description La_Bisbal_dEmpord_nevada
Theme 'La_Bisbal_dEmpord_nevada' by 'Radio Bisbal'. Author's comment
for the theme: Nice pictures taken after snowing at La Bisbal
d'Emporda (Catalonian town).

%description La_Bisbal_dEmpord_nevada -l pl.UTF-8
Motyw 'La_Bisbal_dEmpord_nevada' autorstwa 'Radio Bisbal'. Komentarz
autora do motywu: Nice pictures taken after snowing at La Bisbal
d'Emporda (Catalonian town).

%package Leon
Summary:	Theme Leon for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Leon dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Alvaro del Castillo
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/244/
Requires:	%{name}

%description Leon
Theme 'Leon' by 'Alvaro del Castillo'. Author's comment for the
theme: Leon Spanish city.

%description Leon -l pl.UTF-8
Motyw 'Leon' autorstwa 'Ălvaro del Castillo'. Komentarz autora do
motywu: Leon Spanish city.

%package Linux_Crystal
Summary:	Theme Linux_Crystal for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Linux_Crystal dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Hayl (D K D)
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/588/
Requires:	%{name}

%description Linux_Crystal
Theme 'Linux_Crystal' by 'Hayl (D K D)'. Author's comment for the
theme: Crystal Icons-based GDM theme for GDM 2.4 and higher.

%description Linux_Crystal -l pl.UTF-8
Motyw 'Linux_Crystal' autorstwa 'Hayl (D K D)'. Komentarz autora do
motywu: Crystal Icons-based GDM theme for GDM 2.4 and higher.

%package LinuxTux
Summary:	Theme LinuxTux for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw LinuxTux dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Rebel
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/511/
Requires:	%{name}

%description LinuxTux
Theme 'LinuxTux' by 'Rebel'. Author's comment for the theme: Tux
gdmgreeter.

%description LinuxTux -l pl.UTF-8
Motyw 'LinuxTux' autorstwa 'Rebel'. Komentarz autora do motywu: Tux
gdmgreeter.

%package Luna_GDM_Theme
Summary:	Theme Luna_GDM_Theme for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Luna_GDM_Theme dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Harshwardhan Nagaonkar
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/774/
Requires:	%{name}

%description Luna_GDM_Theme
Theme 'Luna_GDM_Theme' by 'Harshwardhan Nagaonkar'. Author's comment
for the theme: A GDM login screen emulating a popular OS. Also
illustrates the flexibility of the GDM theming engine.

%description Luna_GDM_Theme -l pl.UTF-8
Motyw 'Luna_GDM_Theme' autorstwa 'Harshwardhan Nagaonkar'. Komentarz
autora do motywu: A GDM login screen emulating a popular OS. Also
illustrates the flexibility of the GDM theming engine.

%package M-83
Summary:	Theme M-83 for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw M-83 dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Nexxuz
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/743/
Requires:	%{name}

%description M-83
Theme 'M-83' by 'Nexxuz'. Author's comment for the theme: The well
known spiral galaxy, Messier 83, also known as NGC 5236.

%description M-83 -l pl.UTF-8
Motyw 'M-83' autorstwa 'Nexxuz'. Komentarz autora do motywu: The well
known spiral galaxy, Messier 83, also known as NGC 5236.

%package Machu_Picchu
Summary:	Theme Machu_Picchu for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Machu_Picchu dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		David Thompson
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/300/
Requires:	%{name}

%description Machu_Picchu
Theme 'Machu_Picchu' by 'David Thompson'. Author's comment for the
theme: Pictures of the Inca remains at Machu Picchu in Peru.

%description Machu_Picchu -l pl.UTF-8
Motyw 'Machu_Picchu' autorstwa 'David Thompson'. Komentarz autora do
motywu: Pictures of the Inca remains at Machu Picchu in Peru.

%package ManzanaTux
Summary:	Theme ManzanaTux for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw ManzanaTux dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Rogelio Domínguez Hernández
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/747/
Requires:	%{name}

%description ManzanaTux
Theme 'ManzanaTux' by 'Rogelio Domínguez Hernández'. Author's
comment for the theme: Theme based in Crystal Theme by Niek van der
Maas. All icons are made by Everaldo - <http://www.everaldo.com/>. The
background is by Bandar Raffa - http://www.sadeem.net/tux.html ).

%description ManzanaTux -l pl.UTF-8
Motyw 'ManzanaTux' autorstwa 'Rogelio DomĂ­nguez HernĂĄndez'.
Komentarz autora do motywu: Theme based in Crystal Theme by Niek van
der Maas. All icons are made by Everaldo - <http://www.everaldo.com/>.
The background is by Bandar Raffa - http://www.sadeem.net/tux.html ).

%package ManzanaTuxBlack
Summary:	Theme ManzanaTuxBlack for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw ManzanaTuxBlack dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Rogelio Domínguez Hernández
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/748/
Requires:	%{name}

%description ManzanaTuxBlack
Theme 'ManzanaTuxBlack' by 'Rogelio Domínguez Hernández'. Author's
comment for the theme: Theme based in Crystal Theme by Niek van der
Maas. All icons are made by Everaldo - http://www.everaldo.com/. The
background is by Bandar Raffa - http://www.sadeem.net/tux.html ).

%description ManzanaTuxBlack -l pl.UTF-8
Motyw 'ManzanaTuxBlack' autorstwa 'Rogelio DomĂ­nguez HernĂĄndez'.
Komentarz autora do motywu: Theme based in Crystal Theme by Niek van
der Maas. All icons are made by Everaldo - <http://www.everaldo.com/>.
The background is by Bandar Raffa - http://www.sadeem.net/tux.html ).

%package Milk
Summary:	Theme Milk for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Milk dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Will Reinhart
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/533/
Requires:	%{name}

%description Milk
Theme 'Milk' by 'Will Reinhart'. Author's comment for the theme: A
graphical greeter theme with face browser. It is based on the
MilkGnome background by [Kony], Bluecurve icons, and the Happy GNOME
GDM theme. Requires GDM 2.4.2.95 or newer.

%description Milk -l pl.UTF-8
Motyw 'Milk' autorstwa 'Will Reinhart'. Komentarz autora do motywu: A
graphical greeter theme with face browser. It is based on the
MilkGnome background by [Kony], Bluecurve icons, and the Happy GNOME
GDM theme. Requires GDM 2.4.2.95 or newer.

%package Mirrored
Summary:	Theme Mirrored for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Mirrored dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Roman Joost
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/448/
Requires:	%{name}

%description Mirrored
Theme 'Mirrored' by 'Roman Joost'. Author's comment for the theme:
Mirrored desktop is a mirrored login screen with comic art. Not all of
the text is mirrored (for usability reasons).

%description Mirrored -l pl.UTF-8
Motyw 'Mirrored' autorstwa 'Roman Joost'. Komentarz autora do motywu:
Mirrored desktop is a mirrored login screen with comic art. Not all of
the text is mirrored (for usability reasons).

%package Mono_Metal
Summary:	Theme Mono_Metal for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Mono_Metal dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		crahs
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/494/
Requires:	%{name}

%description Mono_Metal
Theme 'Mono_Metal' by 'crahs'. Author's comment for the theme: This is
my first theme, for GDM based on mono with metal style.

%description Mono_Metal -l pl.UTF-8
Motyw 'Mono_Metal' autorstwa 'crahs'. Komentarz autora do motywu: This
is my first theme, for GDM based on mono with metal style.

%package Morning_Light
Summary:	Theme Morning_Light for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Morning_Light dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Moses Lei
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/103/
Requires:	%{name}

%description Morning_Light
Theme 'Morning_Light' by 'Moses Lei'. Author's comment for the theme:
Background by Ryan Bliss, <http://www.digitalblasphemy.com/>.

%description Morning_Light -l pl.UTF-8
Motyw 'Morning_Light' autorstwa 'Moses Lei'. Komentarz autora do
motywu: Background by Ryan Bliss, <http://www.digitalblasphemy.com/>.

%package Mozi
Summary:	Theme Mozi for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Mozi dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Soho501
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/325/
Requires:	%{name}

%description Mozi
Theme 'Mozi' by 'Soho501'. Author's comment for the theme: Iguana
eating msn butterfly.

%description Mozi -l pl.UTF-8
Motyw 'Mozi' autorstwa 'Soho501'. Komentarz autora do motywu: Iguana
eating msn butterfly.

%package Murcia
Summary:	Theme Murcia for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Murcia dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Alvaro del Castillo
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/243/
Requires:	%{name}

%description Murcia
Theme 'Murcia' by 'Alvaro del Castillo'. Author's comment for the
theme: Murcia Spanish city.

%description Murcia -l pl.UTF-8
Motyw 'Murcia' autorstwa 'Ălvaro del Castillo'. Komentarz autora do
motywu: Murcia Spanish city.

%package Open_Source_Initiative
Summary:	Theme Open_Source_Initiative for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Open_Source_Initiative dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Bryan W Clark
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/270/
Requires:	%{name}

%description Open_Source_Initiative
Theme 'Open_Source_Initiative' by 'Bryan W Clark'. Author's comment
for the theme: The Open Source Initiative (tm) logo
http://opensource.org/ upgraded with a little GIMP action.

%description Open_Source_Initiative -l pl.UTF-8
Motyw 'Open_Source_Initiative' autorstwa 'Bryan W Clark'. Komentarz
autora do motywu: The Open Source Initiative (tm) logo
http://opensource.org/ upgraded with a little GIMP action.

%package Penguin_Computing
Summary:	Theme Penguin_Computing for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Penguin_Computing dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Lars Strojny
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/272/
Requires:	%{name}

%description Penguin_Computing
Theme 'Penguin_Computing' by 'Lars Strojny'. Author's comment for the
theme: Theme with funny Quake-porting-image.

%description Penguin_Computing -l pl.UTF-8
Motyw 'Penguin_Computing' autorstwa 'Lars Strojny'. Komentarz autora
do motywu: Theme with funny Quake-porting-image.

%package Peppe_for_Gonme
Summary:	Theme Peppe_for_Gonme for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Peppe_for_Gonme dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Peppe
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/754/
Requires:	%{name}

%description Peppe_for_Gonme
Theme 'Peppe_for_Gonme' by 'Peppe'. Author's comment for the theme: My
first work.

%description Peppe_for_Gonme -l pl.UTF-8
Motyw 'Peppe_for_Gonme' autorstwa 'Peppe'. Komentarz autora do motywu:
My first work.

%package pixelGDM
Summary:	Theme pixelGDM for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw pixelGDM dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Roman Joost
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/463/
Requires:	%{name}

%description pixelGDM
Theme 'pixelGDM' by 'Roman Joost'. Author's comment for the theme:
pixelGDM is a theme with pixel icons.

%description pixelGDM -l pl.UTF-8
Motyw 'pixelGDM' autorstwa 'Roman Joost'. Komentarz autora do motywu:
pixelGDM is a theme with pixel icons.

%package Red_Leaves
Summary:	Theme Red_Leaves for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Red_Leaves dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Christopher "3-D" Fowler
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/464/
Requires:	%{name}

%description Red_Leaves
Theme 'Red_Leaves' by 'Christopher "3-D" Fowler'. Author's comment for
the theme: Japanese maple Red on a crisp blue fall sky makes a great
greeter.

%description Red_Leaves -l pl.UTF-8
Motyw 'Red_Leaves' autorstwa 'Christopher "3-D" Fowler'. Komentarz
autora do motywu: Japanese maple Red on a crisp blue fall sky makes a
great greeter.

%package RightVision
Summary:	Theme RightVision for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw RightVision dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Thibaut Dabonneville & Alexandre Notteau
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/301/
Requires:	%{name}

%description RightVision
Motyw 'RightVision' by 'Thibaut Dabonneville & Alexandre Notteau'.
Authors' comment for the theme: A colorfull theme used by Linux users
@ RightVision.

%description RightVision -l pl.UTF-8
Motyw 'RightVision' autorstwa 'Thibaut Dabonneville & Alexandre
Notteau'. Komentarz autorów do motywu: A colorfull theme used by Linux
users @ RightVision.

%package Sea
Summary:	Theme Sea for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Sea dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Gianluca Masci
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/107/
Requires:	%{name}

%description Sea
Theme 'Sea' by 'Gianluca Masci'. Author's comment for the theme: A
"Sea and Sunset" theme.

%description Sea -l pl.UTF-8
Motyw 'Sea' autorstwa 'Gianluca Masci'. Komentarz autora do motywu: A
"Sea and Sunset" theme.

%package Segovia
Summary:	Theme Segovia for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Segovia dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Alvaro del Castillo
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/111/
Requires:	%{name}

%description Segovia
Theme 'Segovia' by 'Alvaro del Castillo'. Author's comment for the
theme: A Spanish historical city.

%description Segovia -l pl.UTF-8
Motyw 'Segovia' autorstwa 'Alvaro del Castillo'. Komentarz autora do
motywu: A Spanish historical city.

%package Segovia_Night
Summary:	Theme Segovia_Night for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Segovia_Night dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Alvaro del Castillo
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/108/
Requires:	%{name}

%description Segovia_Night
Theme 'Segovia_Night' by 'Alvaro del Castillo'. Author's comment for
the theme: A Spanish historical city in the night.

%description Segovia_Night -l pl.UTF-8
Motyw 'Segovia_Night' autorstwa 'Alvaro del Castillo'. Komentarz
autora do motywu: A Spanish historical city in the night.

%package Shapy
Summary:	Theme Shapy for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Shapy dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		T.Thiessens
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/776/
Requires:	%{name}

%description Shapy
Theme 'Shapy' by 'T.Thiessens' Author's comment for the theme: Shapy
and colorful.

%description Shapy -l pl.UTF-8
Motyw 'Shapy' autorstwa 'T.Thiessens'. Komentarz autora do motywu:
Shapy and colorful.

%package Simple-Gnome-Logo
Summary:	Theme Simple-GNOME-Logo for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Simple-GNOME-Logo dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Theme by DekuHaze - Background (c) 2003 Bryan W. C
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/617/
Requires:	%{name}

%description Simple-Gnome-Logo
Theme 'Simple-Gnome-Logo' by 'Theme by DekuHaze - Background (c) 2003
Bryan W. C'. Author's comment for the theme: A simple GDM theme based
on the desktop background (Simple Black with Gnome Foot -
http://art.gnome.org/backgrounds/gnome/128.php ) created by Bryan W.
Clark.

%description Simple-Gnome-Logo -l pl.UTF-8
Motyw 'Simple-Gnome-Logo' autorstwa 'Theme by DekuHaze - Background
(c) 2003 Bryan W. C'. Komentarz autora do motywu: A simple GDM theme
based on the desktop background (Simple Black with Gnome Foot -
http://art.gnome.org/backgrounds/gnome/128.php ) created by Bryan W.
Clark.

%package Space
Summary:	Theme Space for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Space dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Guille (bisho)
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/222/
Requires:	%{name}

%description Space
Theme 'Space' by 'Guille (bisho)'. Author's comment for the theme: A
space based greeter with icons borrowed from other themes.

%description Space -l pl.UTF-8
Motyw 'Space' autorstwa 'Guille (bisho)'. Komentarz autora do motywu:
A space based greeter with icons borrowed from other themes.

%package SpreadFirefox
Summary:	Theme SpreadFirefox for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw SpreadFirefox dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		DekuHaze
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/744/
Requires:	%{name}

%description SpreadFirefox
Theme 'SpreadFirefox' by 'DekuHaze'. Author's comment for the theme:
My personal contribution to the 'Spread Firefox' project using the
wallpaper designed by LouCypher. Enjoy.

%description SpreadFirefox -l pl.UTF-8
Motyw 'SpreadFirefox' autorstwa 'DekuHaze'. Komentarz autora do
motywu: My personal contribution to the 'Spread Firefox' project using
the wallpaper designed by LouCypher. Enjoy.

%package STGO
Summary:	Theme STGO for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw STGO dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Phillip
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/109/
Requires:	%{name}

%description STGO
Theme 'STGO' by 'Phillip'. Author's comment for the theme: A photo
from Santiago.

%description STGO -l pl.UTF-8
Motyw 'STGO' autorstwa 'Phillip'. Komentarz autora do motywu: A photo
from Santiago.

%package Stop_TCPA
Summary:	Theme Stop_TCPA for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Stop_TCPA dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Lars Strojny
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/267/
Requires:	%{name}

%description Stop_TCPA
Theme 'Stop_TCPA' by 'Lars Strojny'. Author's comment for the theme: A
Theme against TCPA, Palladium and Censorship.

%description Stop_TCPA -l pl.UTF-8
Motyw 'Stop_TCPA' autorstwa 'Lars Strojny'. Komentarz autora do
motywu: A Theme against TCPA, Palladium and Censorship.

%package SVG_Sakura
Summary:	Theme SVG_Sakura for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw SVG_Sakura dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Ben
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/746/
Requires:	%{name}

%description SVG_Sakura
Theme 'SVG_Sakura' by 'Ben'. Author's comment for the theme: A cherry
blossom theme using exclusively SVG images.

%description SVG_Sakura -l pl.UTF-8
Motyw 'SVG_Sakura' autorstwa 'Ben'. Komentarz autora do motywu: A
cherry blossom theme using exclusively SVG images.

%package Synergy
Summary:	Theme Synergy for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Synergy dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		jam
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/419/
Requires:	%{name}

%description Synergy
Theme 'Synergy' by 'jam'. Author's comment for the theme: Synergy:
cube showing 2 faces. KDE logo on left face, Gnome logo on the other.

%description Synergy -l pl.UTF-8
Motyw 'Synergy' autorstwa 'jam'. Komentarz autora do motywu: Synergy:
cube showing 2 faces. KDE logo on left face, Gnome logo on the other.

%package Taipei
Summary:	Theme Taipei for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Taipei dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Julian Coccia
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/525/
Requires:	%{name}

%description Taipei
Theme 'Taipei' by 'Julian Coccia'. Author's comment for the theme:
Taipei, CKS Memorial Entrance (1600x1200).

%description Taipei -l pl.UTF-8
Motyw 'Taipei' autorstwa 'Julian Coccia'. Komentarz autora do motywu:
Taipei, CKS Memorial Entrance (1600x1200).

%package The_Dark_Crystal
Summary:	Theme The_Dark_Crystal for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw The_Dark_Crystal dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Bobby Corbell
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/293/
Requires:	%{name}

%description The_Dark_Crystal
Theme 'The_Dark_Crystal' by 'Bobby Corbell'. Author's comment for the
theme: A collage of images from the movie The Dark Crystal.

%description The_Dark_Crystal -l pl.UTF-8
Motyw 'The_Dark_Crystal' autorstwa 'Bobby Corbell'. Komentarz autora
do motywu: A collage of images from the movie The Dark Crystal.

%package Todmorden
Summary:	Theme Todmorden for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Todmorden dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Todd Jones
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/332/
Requires:	%{name}

%description Todmorden
Theme 'Todmorden' by 'Todd Jones'. Author's comment for the theme: A
pic I took from a hill over Todmorden, England.

%description Todmorden -l pl.UTF-8
Motyw 'Todmorden' autorstwa 'Todd Jones'. Komentarz autora do motywu:
A pic I took from a hill over Todmorden, England.

%package Valladolid
Summary:	Theme Valladolid for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw Valladolid dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Alvaro del Castillo
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/242/
Requires:	%{name}

%description Valladolid
Theme 'Valladolid' by 'Alvaro del Castillo'. Author's comment for
the theme: Valladolid Spanish city.

%description Valladolid -l pl.UTF-8
Motyw 'Valladolid' autorstwa 'Ălvaro del Castillo'. Komentarz autora
do motywu: Valladolid Spanish city.

%package XPTO
Summary:	Theme XPTO for gdm (GNOME Display Manager)
Summary(pl.UTF-8):	Motyw XPTO dla gdm (Zarządcy ekranów GNOME)
License:	GPL
Vendor:		Nelson Marques
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/182/
Requires:	%{name}

%description XPTO
Theme 'XPTO' by 'Nelson Marques'. Author's comment for the theme: A
theme made for the common GDM logins of our humble machines.

%description XPTO -l pl.UTF-8
Motyw 'XPTO' autorstwa 'Nelson Marques'. Komentarz autora do motywu: A
theme made for the common GDM logins of our humble machines.

%prep
%setup -q -c %{_builddir}/%{name}-%{version}  -a0 -a1 -a2 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31 -a32 -a33 -a34 -a35 -a36 -a37 -a38 -a39 -a40 -a41 -a42 -a43 -a44 -a45 -a46 -a47 -a48 -a49 -a50 -a51 -a52 -a53 -a54 -a55 -a56 -a57 -a58 -a59 -a60 -a61 -a62 -a63 -a64 -a65 -a66 -a67 -a68 -a69 -a71 -a72 -a73 -a74 -a75 -a76 -a77 -a78 -a79 -a80

cat>README<<E_O_F
This is small x-mas gift from yoshi to all PLD users, developers and
enthusiasts ;-)
Have fun and support art.gnome.org with your own creations (if you can).

Merry Christmas :)
E_O_F

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes
#
# Theme 00/80
#
# Make '300-lantueno' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/300-lantueno
# Install '300-lantueno' theme files
install lantueno-gdm/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/300-lantueno
install lantueno-gdm/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/300-lantueno
install lantueno-gdm/lantueno.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/300-lantueno
install lantueno-gdm/lantueno.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/300-lantueno
install lantueno-gdm/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/300-lantueno
install lantueno-gdm/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/300-lantueno
install lantueno-gdm/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/300-lantueno
install lantueno-gdm/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/300-lantueno
install lantueno-gdm/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/300-lantueno
#
# Theme 01/80
#
# Make '9nome-Darmis' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/9nome-Darmis
# Install '9nome-Darmis' theme files
install 9nome-Darmis/background.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/9nome-Darmis
install 9nome-Darmis/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/9nome-Darmis
install 9nome-Darmis/gdm-theme.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/9nome-Darmis
install 9nome-Darmis/halt.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/9nome-Darmis
install 9nome-Darmis/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/9nome-Darmis
install 9nome-Darmis/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/9nome-Darmis
install 9nome-Darmis/reboot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/9nome-Darmis
install 9nome-Darmis/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/9nome-Darmis
install 9nome-Darmis/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/9nome-Darmis
#
# Theme 02/80
#
# Make 'Angel' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Angel
# Install 'Angel' theme files
install Angel/angel.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Angel
install Angel/angel.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Angel
install Angel/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Angel
install Angel/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Angel
install Angel/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Angel
install Angel/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Angel
install Angel/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Angel
install Angel/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Angel
install Angel/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Angel
#
# Theme 03/80
#
# Make 'Barcelona' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Barcelona
# Install 'Barcelona' theme files
#
# Theme 04/80
#
# Make 'Bee_at_Work' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bee_at_Work
# Install 'Bee_at_Work' theme files
install BeeAtWork/background.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bee_at_Work
install BeeAtWork/BeeAtWork.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bee_at_Work
install BeeAtWork/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bee_at_Work
install BeeAtWork/help.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bee_at_Work
install BeeAtWork/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bee_at_Work
install BeeAtWork/theme.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bee_at_Work
#
# Theme 05/80
#
# Make 'Bijou' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bijou
# Install 'Bijou' theme files
install bijou/background.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bijou
install bijou/bijou.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bijou
install bijou/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bijou
install bijou/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bijou
install bijou/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bijou
install bijou/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bijou
install bijou/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bijou
install bijou/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Bijou
#
# Theme 06/80
#
# Make 'Blueish' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Blueish
# Install 'Blueish' theme files
install bluish-gdm/bluish-gdm.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Blueish
install bluish-gdm/bluish.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Blueish
install bluish-gdm/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Blueish
install bluish-gdm/help.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Blueish
install bluish-gdm/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Blueish
install bluish-gdm/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Blueish
install bluish-gdm/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Blueish
install bluish-gdm/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Blueish
install bluish-gdm/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Blueish
#
# Theme 07/80
#
# Make 'Butterfly' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Butterfly
# Install 'Butterfly' theme files
install butterfly/bfly.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Butterfly
install butterfly/butterfly.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Butterfly
install butterfly/butterfly_tahoma.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Butterfly
install butterfly/butterfly.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Butterfly
install butterfly/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Butterfly
install butterfly/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Butterfly
install butterfly/option.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Butterfly
install butterfly/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Butterfly
install butterfly/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Butterfly
#
# Theme 08/80
#
# Make 'Colorado_Windmill' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Colorado_Windmill
# Install 'Colorado_Windmill' theme files
install Windmill/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Colorado_Windmill
install Windmill/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Colorado_Windmill
install Windmill/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Colorado_Windmill
install Windmill/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Colorado_Windmill
install Windmill/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Colorado_Windmill
install Windmill/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Colorado_Windmill
install Windmill/windmill.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Colorado_Windmill
install Windmill/windmill-screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Colorado_Windmill
install Windmill/Windmill.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Colorado_Windmill
#
# Theme 09/80
#
# Make 'Cracked_Windows' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cracked_Windows
# Install 'Cracked_Windows' theme files
install cracked-windows/cracked-windows.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cracked_Windows
install cracked-windows/cracked-windows.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cracked_Windows
install cracked-windows/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cracked_Windows
install cracked-windows/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cracked_Windows
install cracked-windows/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cracked_Windows
install cracked-windows/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cracked_Windows
install cracked-windows/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cracked_Windows
install cracked-windows/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cracked_Windows
#
# Theme 10/80
#
# Make 'Crop_Circles' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
# Install 'Crop_Circles' theme files
install ./cropcircles/background.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
install ./cropcircles/Bottombar.svg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
install ./cropcircles/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
install ./cropcircles/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
install ./cropcircles/gnome-logo.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
install ./cropcircles/halt.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
install ./cropcircles/lang.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
install ./cropcircles/List.svg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
install ./cropcircles/Login.svg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
install ./cropcircles/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
install ./cropcircles/readme $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
install ./cropcircles/reboot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
install ./cropcircles/roundrect.svg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
install ./cropcircles/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
install ./cropcircles/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
install ./cropcircles/signs.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
install ./cropcircles/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
install ./cropcircles/Topbar.svg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crop_Circles
#
# Theme 11/80
#
# Make 'Crystal' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal
# Install 'Crystal' theme files
install crystal/background.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal
install crystal/Crystal.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal
install crystal/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal
install crystal/galikynes.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal
install crystal/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal
install crystal/option.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal
install crystal/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal
install crystal/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal
install crystal/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal
#
# Theme 12/80
#
# Make 'Crystal_For_Gnome' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_For_Gnome
# Install 'Crystal_For_Gnome' theme files
install "Crystal for Gnome/Acknowlagements" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_For_Gnome
install "Crystal for Gnome/background.png" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_For_Gnome
install "Crystal for Gnome/Crystal_for_Gnome.xml" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_For_Gnome
install "Crystal for Gnome/disconnect.png" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_For_Gnome
install "Crystal for Gnome/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_For_Gnome
install "Crystal for Gnome/halt.png" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_For_Gnome
install "Crystal for Gnome/options.png" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_For_Gnome
install "Crystal for Gnome/reboot.png" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_For_Gnome
install "Crystal for Gnome/screenshot.png" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_For_Gnome
install "Crystal for Gnome/session.png" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_For_Gnome
install "Crystal for Gnome/system.png" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_For_Gnome
#
# Theme 13/80
#
# Make 'Crystal_for_Gnome_-_theme_2' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2
# Install 'Crystal_for_Gnome_-_theme_2' theme files
install CrystalforGnome2/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2
install CrystalforGnome2/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2
install CrystalforGnome2/gentoo.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2
install CrystalforGnome2/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2
install CrystalforGnome2/loginbox.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2
install CrystalforGnome2/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2
install CrystalforGnome2/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2
install CrystalforGnome2/theme.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2
install CrystalforGnome2/wall.svg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2
#
# Theme 14/80
#
# Make 'Crystal_Rose' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_Rose
# Install 'Crystal_Rose' theme files
install crystal-rose/crystal-rose.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_Rose
install crystal-rose/crystal-rose.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_Rose
install crystal-rose/crystal-rose-screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_Rose
install crystal-rose/crystal-rose.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_Rose
install crystal-rose/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_Rose
install crystal-rose/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_Rose
install crystal-rose.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Crystal_Rose
#
# Theme 15/80
#
# Make 'Cubic_Linux_and_Gnome' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome
# Install 'Cubic_Linux_and_Gnome' theme files
install Cubic_Linux_Gnome/background.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome
install Cubic_Linux_Gnome/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome
install Cubic_Linux_Gnome/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome
install Cubic_Linux_Gnome/halt.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome
install Cubic_Linux_Gnome/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome
install Cubic_Linux_Gnome/reboot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome
install Cubic_Linux_Gnome/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome
install Cubic_Linux_Gnome/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome
install Cubic_Linux_Gnome/theme.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome
#
# Theme 16/80
#
# Make 'Dart_Frog' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dart_Frog
# Install 'Dart_Frog' theme files
install dartfrog/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dart_Frog
install dartfrog/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dart_Frog
install dartfrog/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dart_Frog
install dartfrog/pitcherplant.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dart_Frog
install dartfrog/pitcherplant.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dart_Frog
install dartfrog/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dart_Frog
install dartfrog/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dart_Frog
install dartfrog/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dart_Frog
install dartfrog/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dart_Frog
#
# Theme 17/80
#
# Make 'Dawn' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dawn
# Install 'Dawn' theme files
install dawn/background.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dawn
install dawn/dawn.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dawn
install dawn/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dawn
install dawn/option.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dawn
install dawn/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dawn
install dawn/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dawn
install dawn/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dawn
install dawn/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dawn
#
# Theme 18/80
#
# Make 'Daybreak' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Daybreak
# Install 'Daybreak' theme files
install daybreak/daybreak.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Daybreak
install daybreak/daybreak.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Daybreak
install daybreak/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Daybreak
install daybreak/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Daybreak
install daybreak/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Daybreak
install daybreak/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Daybreak
install daybreak/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Daybreak
install daybreak/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Daybreak
install daybreak/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Daybreak
#
# Theme 19/80
#
# Make 'Delicious' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Delicious
# Install 'Delicious' theme files
install delicious-theme/delicious.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Delicious
install delicious-theme/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Delicious
install delicious-theme/head1.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Delicious
install delicious-theme/mampf.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Delicious
install delicious-theme/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Delicious
install delicious-theme/screenshot-small.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Delicious
install delicious-theme/sys.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Delicious
#
# Theme 20/80
#
# Make 'Devils_Candy' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Devils_Candy
# Install 'Devils_Candy' theme files
install DevilsCandy/background.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Devils_Candy
install DevilsCandy/ball.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Devils_Candy
install DevilsCandy/devil.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Devils_Candy
install DevilsCandy/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Devils_Candy
install DevilsCandy/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Devils_Candy
install DevilsCandy/option.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Devils_Candy
install DevilsCandy/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Devils_Candy
install DevilsCandy/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Devils_Candy
install DevilsCandy/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Devils_Candy
#
# Theme 21/80
#
# Make 'Dreaming_Alien' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dreaming_Alien
# Install 'Dreaming_Alien' theme files
install usr/share/gdm/themes/dreaming-alien/background.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dreaming_Alien
install usr/share/gdm/themes/dreaming-alien/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dreaming_Alien
install usr/share/gdm/themes/dreaming-alien/dreaming-alien.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dreaming_Alien
install usr/share/gdm/themes/dreaming-alien/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dreaming_Alien
install usr/share/gdm/themes/dreaming-alien/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dreaming_Alien
install usr/share/gdm/themes/dreaming-alien/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dreaming_Alien
install usr/share/gdm/themes/dreaming-alien/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dreaming_Alien
install usr/share/gdm/themes/dreaming-alien/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Dreaming_Alien
#
# Theme 22/80
#
# Make 'DumbCloud' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/DumbCloud
# Install 'DumbCloud' theme files
install dumbcloud/cloud2.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/DumbCloud
install dumbcloud/dumbcloud.svg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/DumbCloud
install dumbcloud/dumbcloud.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/DumbCloud
install dumbcloud/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/DumbCloud
install dumbcloud/help.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/DumbCloud
install dumbcloud/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/DumbCloud
install dumbcloud/test2.svg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/DumbCloud
#
# Theme 23/80
#
# Make 'Emo-Blue' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Emo-Blue
# Install 'Emo-Blue' theme files
install emo-blue/emo-blue.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Emo-Blue
install emo-blue/emo-blue.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Emo-Blue
install emo-blue/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Emo-Blue
install emo-blue/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Emo-Blue
install emo-blue/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Emo-Blue
install emo-blue/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Emo-Blue
install emo-blue/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Emo-Blue
install emo-blue/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Emo-Blue
install emo-blue/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Emo-Blue
#
# Theme 24/80
#
# Make 'Falling_Angel' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Falling_Angel
# Install 'Falling_Angel' theme files
install falling-angel/falling-angel.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Falling_Angel
install falling-angel/falling-angel-shot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Falling_Angel
install falling-angel/falling-angel.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Falling_Angel
install falling-angel/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Falling_Angel
install falling-angel/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Falling_Angel
install falling-angel/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Falling_Angel
install falling-angel/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Falling_Angel
install falling-angel/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Falling_Angel
install falling-angel/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Falling_Angel
#
# Theme 25/80
#
# Make 'Fire_Breathing_Robot' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Fire_Breathing_Robot
# Install 'Fire_Breathing_Robot' theme files
install flame/flames.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Fire_Breathing_Robot
install flame/flame.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Fire_Breathing_Robot
install flame/gdmbar.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Fire_Breathing_Robot
install flame/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Fire_Breathing_Robot
install flame/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Fire_Breathing_Robot
install flame/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Fire_Breathing_Robot
install flame/shadow-bl.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Fire_Breathing_Robot
install flame/shadow-b.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Fire_Breathing_Robot
install flame/shadow-br.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Fire_Breathing_Robot
install flame/shadow-l.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Fire_Breathing_Robot
install flame/shadow-r.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Fire_Breathing_Robot
install flame/shadow-tl.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Fire_Breathing_Robot
install flame/shadow-t.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Fire_Breathing_Robot
install flame/shadow-tr.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Fire_Breathing_Robot
#
# Theme 26/80
#
# Make 'Flowers' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Flowers
# Install 'Flowers' theme files
install flowers/background.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Flowers
install flowers/flowers.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Flowers
install flowers/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Flowers
install flowers/help.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Flowers
install flowers/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Flowers
install flowers/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Flowers
install flowers/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Flowers
#
# Theme 27/80
#
# Make 'gcr-ddlm' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/gcr-ddlm
# Install 'gcr-ddlm' theme files
install gcr-ddlm/gcr-ddlm.background.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/gcr-ddlm
install gcr-ddlm/gcr-ddlm.background.screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/gcr-ddlm
install gcr-ddlm/gcr-ddlm.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/gcr-ddlm
install gcr-ddlm/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/gcr-ddlm
install gcr-ddlm/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/gcr-ddlm
install gcr-ddlm/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/gcr-ddlm
install gcr-ddlm/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/gcr-ddlm
install gcr-ddlm/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/gcr-ddlm
#
# Theme 28/80
#
# Make 'Gdm_Dropline' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gdm_Dropline
# Install 'Gdm_Dropline' theme files
install gdm-dropline/dropline-blue.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gdm_Dropline
install gdm-dropline/dropline-blue.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gdm_Dropline
install gdm-dropline/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gdm_Dropline
install gdm-dropline/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gdm_Dropline
install gdm-dropline/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gdm_Dropline
install gdm-dropline/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gdm_Dropline
install gdm-dropline/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gdm_Dropline
install gdm-dropline/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gdm_Dropline
install gdm-dropline/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gdm_Dropline
#
# Theme 29/80
#
# Make 'GDM_Waves' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM_Waves
# Install 'GDM_Waves' theme files
install GDM-Waves/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM_Waves
install GDM-Waves/gdm-waves.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM_Waves
install GDM-Waves/gdm-waves-screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM_Waves
install GDM-Waves/gdm-waves.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM_Waves
install GDM-Waves/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM_Waves
install GDM-Waves/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM_Waves
install GDM-Waves/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM_Waves
install GDM-Waves/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM_Waves
install GDM-Waves/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM_Waves
#
# Theme 30/80
#
# Make 'GDM-GlassFoot' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-GlassFoot
# Install 'GDM-GlassFoot' theme files
install GNOME-GlassFoot/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-GlassFoot
install GNOME-GlassFoot/glass.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-GlassFoot
install GNOME-GlassFoot/GNOME-GlassFoot.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-GlassFoot
install GNOME-GlassFoot/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-GlassFoot
install GNOME-GlassFoot/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-GlassFoot
install GNOME-GlassFoot/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-GlassFoot
install GNOME-GlassFoot/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-GlassFoot
install GNOME-GlassFoot/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-GlassFoot
#
# Theme 31/80
#
# Make 'GDM-Mosaic' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-Mosaic
# Install 'GDM-Mosaic' theme files
install Mosaic/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-Mosaic
install Mosaic/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-Mosaic
install Mosaic/Mosaic.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-Mosaic
install Mosaic/Mosaic.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-Mosaic
install Mosaic/option.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-Mosaic
install Mosaic/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-Mosaic
install Mosaic/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-Mosaic
install Mosaic/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/GDM-Mosaic
#
# Theme 32/80
#
# Make 'Glassy' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Glassy
# Install 'Glassy' theme files
install Glassy/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Glassy
install Glassy/glassy.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Glassy
install Glassy/glassy.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Glassy
install Glassy/help.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Glassy
install Glassy/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Glassy
install Glassy/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Glassy
install Glassy/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Glassy
install Glassy/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Glassy
install Glassy/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Glassy
#
# Theme 33/80
#
# Make 'Gnome_Chile' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Chile
# Install 'Gnome_Chile' theme files
install gnome-chile/fondo.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Chile
install gnome-chile/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Chile
install gnome-chile/gnome-chile.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Chile
install gnome-chile/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Chile
install gnome-chile/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Chile
install gnome-chile/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Chile
install gnome-chile/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Chile
install gnome-chile/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Chile
install gnome-chile/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Chile
#
# Theme 34/80
#
# Make 'Gnome_Plain_Swoosh_GDM_Theme' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme
# Install 'Gnome_Plain_Swoosh_GDM_Theme' theme files
install GDM-plain-swoosh/background.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme
install GDM-plain-swoosh/curve-bottom_left.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme
install GDM-plain-swoosh/curve-bottom_right.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme
install GDM-plain-swoosh/curve-top_left.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme
install GDM-plain-swoosh/curve-top_right.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme
install GDM-plain-swoosh/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme
install GDM-plain-swoosh/options1.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme
install GDM-plain-swoosh/options2.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme
install GDM-plain-swoosh/options_hilite1.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme
install GDM-plain-swoosh/options_hilite2.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme
install GDM-plain-swoosh/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme
install GDM-plain-swoosh/swoosh.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme
#
# Theme 35/80
#
# Make 'Gnome_Plain_Swoosh_GDM_Theme_TNG' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG
# Install 'Gnome_Plain_Swoosh_GDM_Theme_TNG' theme files
install GDM-plain-swoosh-tng/background.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG
install GDM-plain-swoosh-tng/dashed-rect.svg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG
install GDM-plain-swoosh-tng/dotline.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG
install GDM-plain-swoosh-tng/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG
install GDM-plain-swoosh-tng/gnome-linux-desktop.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG
install GDM-plain-swoosh-tng/plain-swoosh-tng.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG
install GDM-plain-swoosh-tng/README $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG
install GDM-plain-swoosh-tng/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG
install GDM-plain-swoosh-tng/shade-left.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG
install GDM-plain-swoosh-tng/shade-right.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG
install GDM-plain-swoosh-tng/small-n.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG
install GDM-plain-swoosh-tng/vline.svg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG
#
# Theme 36/80
#
# Make 'Hantzley' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Hantzley
# Install 'Hantzley' theme files
install Hantzley/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Hantzley
install Hantzley/hantzley.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Hantzley
install Hantzley/hantzley.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Hantzley
install Hantzley/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Hantzley
install Hantzley/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Hantzley
install Hantzley/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Hantzley
install Hantzley/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Hantzley
install Hantzley/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Hantzley
install Hantzley/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Hantzley
#
# Theme 37/80
#
# Make 'Hunter' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Hunter
# Install 'Hunter' theme files
install hunter/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Hunter
install hunter/help.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Hunter
install hunter/hunter.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Hunter
install hunter/hunter.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Hunter
install hunter/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Hunter
install hunter/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Hunter
#
# Theme 38/80
#
# Make 'hybridFUSION' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/hybridFUSION
# Install 'hybridFUSION' theme files
install hybridFUSION/ConVerSion_version_Two.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/hybridFUSION
install hybridFUSION/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/hybridFUSION
install hybridFUSION/hybridFUSION.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/hybridFUSION
install hybridFUSION/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/hybridFUSION
install hybridFUSION/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/hybridFUSION
install hybridFUSION/shadow-bl.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/hybridFUSION
install hybridFUSION/shadow-b.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/hybridFUSION
install hybridFUSION/shadow-br.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/hybridFUSION
install hybridFUSION/shadow-l.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/hybridFUSION
install hybridFUSION/shadow-r.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/hybridFUSION
install hybridFUSION/shadow-tl.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/hybridFUSION
install hybridFUSION/shadow-t.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/hybridFUSION
install hybridFUSION/shadow-tr.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/hybridFUSION
install hybridFUSION/skowals.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/hybridFUSION
#
# Theme 39/80
#
# Make 'In_This_World' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/In_This_World
# Install 'In_This_World' theme files
install InThisWorld/background.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/In_This_World
install InThisWorld/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/In_This_World
install InThisWorld/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/In_This_World
install InThisWorld/InThisWorld.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/In_This_World
install InThisWorld/option.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/In_This_World
install InThisWorld/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/In_This_World
install InThisWorld/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/In_This_World
install InThisWorld/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/In_This_World
#
# Theme 40/80
#
# Make 'KDE_Crystal' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/KDE_Crystal
# Install 'KDE_Crystal' theme files
install crystal_gdm/background.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/KDE_Crystal
install crystal_gdm/crystal.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/KDE_Crystal
install crystal_gdm/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/KDE_Crystal
install crystal_gdm/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/KDE_Crystal
install crystal_gdm/halt.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/KDE_Crystal
install crystal_gdm/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/KDE_Crystal
install crystal_gdm/reboot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/KDE_Crystal
install crystal_gdm/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/KDE_Crystal
install crystal_gdm/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/KDE_Crystal
#
# Theme 41/80
#
# Make 'Kinkakuji' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Kinkakuji
# Install 'Kinkakuji' theme files
install kinkakuji/background.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Kinkakuji
install kinkakuji/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Kinkakuji
install kinkakuji/help.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Kinkakuji
install kinkakuji/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Kinkakuji
install kinkakuji/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Kinkakuji
install kinkakuji/theme.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Kinkakuji
#
# Theme 42/80
#
# Make 'Knoke' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Knoke
# Install 'Knoke' theme files
install knoke/back.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Knoke
install knoke/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Knoke
install knoke/knoke.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Knoke
install knoke/knoke.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Knoke
install knoke/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Knoke
install knoke/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Knoke
install knoke/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Knoke
install knoke/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Knoke
install knoke/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Knoke
#
# Theme 43/80
#
# Make 'La_Bisbal_dEmpord_nevada' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada
# Install 'La_Bisbal_dEmpord_nevada' theme files
install labisbal/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada
install labisbal/labisbal-desconectar.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada
install labisbal/labisbal.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada
install labisbal/labisbal-opcions.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada
install labisbal/labisbal-sessio.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada
install labisbal/labisbal-sistema.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada
install labisbal/labisbal.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada
install labisbal/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada
#
# Theme 44/80
#
# Make 'Leon' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Leon
# Install 'Leon' theme files
install leon/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Leon
install leon/leon-desconectar.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Leon
install leon/leon.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Leon
install leon/leon-opciones.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Leon
install leon/leon-sesion.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Leon
install leon/leon-sistema.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Leon
install leon/leon.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Leon
install leon/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Leon
#
# Theme 45/80
#
# Make 'Linux_Crystal' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Linux_Crystal
# Install 'Linux_Crystal' theme files
install Linux_Crystal/background.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Linux_Crystal
install Linux_Crystal/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Linux_Crystal
install Linux_Crystal/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Linux_Crystal
install Linux_Crystal/halt.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Linux_Crystal
install Linux_Crystal/Linux_Crystal.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Linux_Crystal
install Linux_Crystal/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Linux_Crystal
install Linux_Crystal/reboot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Linux_Crystal
install Linux_Crystal/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Linux_Crystal
install Linux_Crystal/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Linux_Crystal
install Linux_Crystal/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Linux_Crystal
#
# Theme 46/80
#
# Make 'LinuxTux' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/LinuxTux
# Install 'LinuxTux' theme files
install linuxtux/background.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/LinuxTux
install linuxtux/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/LinuxTux
install linuxtux/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/LinuxTux
install linuxtux/option.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/LinuxTux
install linuxtux/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/LinuxTux
install linuxtux/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/LinuxTux
install linuxtux/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/LinuxTux
install linuxtux/tux.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/LinuxTux
install linuxtux/tux.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/LinuxTux
#
# Theme 47/80
#
# Make 'Luna_GDM_Theme' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Luna_GDM_Theme
# Install 'Luna_GDM_Theme' theme files
#
# Theme 48/80
#
# Make 'M-83' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/M-83
# Install 'M-83' theme files
install M82/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/M-83
install M82/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/M-83
install M82/space.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/M-83
install M82/Space.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/M-83
install M82/ss.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/M-83
#
# Theme 49/80
#
# Make 'Machu_Picchu' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Machu_Picchu
# Install 'Machu_Picchu' theme files
install "Machu Picchu/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Machu_Picchu
install "Machu Picchu/Machu Picchu.xml" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Machu_Picchu
install "Machu Picchu/MP-ledge-bg.png" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Machu_Picchu
install "Machu Picchu/MP-tall-options.png" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Machu_Picchu
install "Machu Picchu/MP-tall-quit.png" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Machu_Picchu
install "Machu Picchu/MP-tall-session.png" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Machu_Picchu
install "Machu Picchu/MP-tall-system.png" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Machu_Picchu
install "Machu Picchu/screenshot.png" $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Machu_Picchu
#
# Theme 50/80
#
# Make 'ManzanaTux' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTux
# Install 'ManzanaTux' theme files
install manzanatux/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTux
install manzanatux/galikynes.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTux
install manzanatux/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTux
install manzanatux/ManzanaTux.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTux
install manzanatux/option.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTux
install manzanatux/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTux
install manzanatux/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTux
install manzanatux/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTux
install manzanatux/thinkshell.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTux
#
# Theme 51/80
#
# Make 'ManzanaTuxBlack' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTuxBlack
# Install 'ManzanaTuxBlack' theme files
install manzanatuxblack/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTuxBlack
install manzanatuxblack/galikynes.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTuxBlack
install manzanatuxblack/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTuxBlack
install manzanatuxblack/ManzanaTuxBlack.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTuxBlack
install manzanatuxblack/option.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTuxBlack
install manzanatuxblack/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTuxBlack
install manzanatuxblack/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTuxBlack
install manzanatuxblack/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTuxBlack
install manzanatuxblack/thinklinux.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/ManzanaTuxBlack
#
# Theme 52/80
#
# Make 'Milk' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Milk
# Install 'Milk' theme files
install milk/background.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Milk
install milk/background.svg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Milk
install milk/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Milk
install milk/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Milk
install milk/gnome-logo.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Milk
install milk/milk.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Milk
install milk/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Milk
install milk/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Milk
install milk/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Milk
install milk/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Milk
#
# Theme 53/80
#
# Make 'Mirrored' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mirrored
# Install 'Mirrored' theme files
install mirrored-theme/background.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mirrored
install mirrored-theme/COPYING $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mirrored
install mirrored-theme/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mirrored
install mirrored-theme/head1.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mirrored
install mirrored-theme/head3.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mirrored
install mirrored-theme/head4.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mirrored
install mirrored-theme/head5.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mirrored
install mirrored-theme/mirrored.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mirrored
install mirrored-theme/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mirrored
install mirrored-theme/sys.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mirrored
#
# Theme 54/80
#
# Make 'Mono_Metal' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mono_Metal
# Install 'Mono_Metal' theme files
install mono-metal/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mono_Metal
install mono-metal/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mono_Metal
install mono-metal/metal.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mono_Metal
install mono-metal/mono_metal.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mono_Metal
install mono-metal/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mono_Metal
install mono-metal/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mono_Metal
install mono-metal/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mono_Metal
install mono-metal/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mono_Metal
#
# Theme 55/80
#
# Make 'Morning_Light' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Morning_Light
# Install 'Morning_Light' theme files
install morning/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Morning_Light
install morning/help.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Morning_Light
install morning/morning.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Morning_Light
install morning/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Morning_Light
install morning/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Morning_Light
install morning/theme.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Morning_Light
#
# Theme 56/80
#
# Make 'Mozi' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mozi
# Install 'Mozi' theme files
install Mozi/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mozi
install Mozi/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mozi
install Mozi/mozilla.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mozi
install Mozi/option.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mozi
install Mozi/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mozi
install Mozi/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mozi
install Mozi/soho.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mozi
install Mozi/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Mozi
#
# Theme 57/80
#
# Make 'Murcia' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Murcia
# Install 'Murcia' theme files
install murcia/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Murcia
install murcia/murcia-desconectar.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Murcia
install murcia/murcia.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Murcia
install murcia/murcia-opciones.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Murcia
install murcia/murcia-sesion.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Murcia
install murcia/murcia-sistema.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Murcia
install murcia/murcia.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Murcia
install murcia/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Murcia
#
# Theme 58/80
#
# Make 'Open_Source_Initiative' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Open_Source_Initiative
# Install 'Open_Source_Initiative' theme files
install OpenSource/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Open_Source_Initiative
install OpenSource/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Open_Source_Initiative
install OpenSource/open_source.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Open_Source_Initiative
install OpenSource/open_source.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Open_Source_Initiative
install OpenSource/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Open_Source_Initiative
install OpenSource/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Open_Source_Initiative
install OpenSource/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Open_Source_Initiative
install OpenSource/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Open_Source_Initiative
install OpenSource/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Open_Source_Initiative
#
# Theme 59/80
#
# Make 'Penguin_Computing' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Penguin_Computing
# Install 'Penguin_Computing' theme files
install penguin/background.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Penguin_Computing
install penguin/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Penguin_Computing
install penguin/galikynes.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Penguin_Computing
install penguin/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Penguin_Computing
install penguin/option.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Penguin_Computing
install penguin/penguin.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Penguin_Computing
install penguin/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Penguin_Computing
install penguin/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Penguin_Computing
#
# Theme 60/80
#
# Make 'Peppe_for_Gonme' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Peppe_for_Gonme
# Install 'Peppe_for_Gonme' theme files
install PeppeforGnome/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Peppe_for_Gonme
install PeppeforGnome/lingua.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Peppe_for_Gonme
install PeppeforGnome/login.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Peppe_for_Gonme
install PeppeforGnome/logo.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Peppe_for_Gonme
install PeppeforGnome/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Peppe_for_Gonme
install PeppeforGnome/servizi.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Peppe_for_Gonme
install PeppeforGnome/sessioni.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Peppe_for_Gonme
install PeppeforGnome/sfondo.svg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Peppe_for_Gonme
install PeppeforGnome/theme.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Peppe_for_Gonme
#
# Theme 61/80
#
# Make 'pixelGDM' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/pixelGDM
# Install 'pixelGDM' theme files
install pixelGDM/background.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/pixelGDM
install pixelGDM/disconnect_over.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/pixelGDM
install pixelGDM/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/pixelGDM
install pixelGDM/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/pixelGDM
install pixelGDM/language_over.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/pixelGDM
install pixelGDM/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/pixelGDM
install pixelGDM/pixelGDM.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/pixelGDM
install pixelGDM/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/pixelGDM
install pixelGDM/screenshot-small.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/pixelGDM
install pixelGDM/session_over.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/pixelGDM
install pixelGDM/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/pixelGDM
install pixelGDM/shutdown_over.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/pixelGDM
install pixelGDM/shutdown.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/pixelGDM
install pixelGDM/system_over.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/pixelGDM
install pixelGDM/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/pixelGDM
#
# Theme 62/80
#
# Make 'Red_Leaves' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Red_Leaves
# Install 'Red_Leaves' theme files
install leaves/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Red_Leaves
install leaves/leaves.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Red_Leaves
install leaves/leaves-screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Red_Leaves
install leaves/leaves.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Red_Leaves
install leaves/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Red_Leaves
#
# Theme 63/80
#
# Make 'RightVision' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/RightVision
# Install 'RightVision' theme files
install RV/background.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/RightVision
install RV/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/RightVision
install RV/logorv.gif $RPM_BUILD_ROOT%{_datadir}/gdm/themes/RightVision
install RV/oeil1.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/RightVision
install RV/oeil2.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/RightVision
install RV/oeil3.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/RightVision
install RV/oeil4.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/RightVision
install RV/rv.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/RightVision
install RV/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/RightVision
#
# Theme 64/80
#
# Make 'Sea' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Sea
# Install 'Sea' theme files
install sea/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Sea
install sea/help.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Sea
install sea/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Sea
install sea/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Sea
install sea/sea.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Sea
install sea/sea.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Sea
#
# Theme 65/80
#
# Make 'Segovia' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia
# Install 'Segovia' theme files
install segovia/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia
install segovia/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia
install segovia/segovia1.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia
install segovia/segovia2.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia
install segovia/segovia3.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia
install segovia/segovia4.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia
install segovia/segovia.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia
install segovia/segovia.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia
#
# Theme 66/80
#
# Make 'Segovia_Night' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia_Night
# Install 'Segovia_Night' theme files
install segovia-night/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia_Night
install segovia-night/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia_Night
install segovia-night/segovia1.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia_Night
install segovia-night/segovia2.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia_Night
install segovia-night/segovia3.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia_Night
install segovia-night/segovia4.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia_Night
install segovia-night/segovia-night.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia_Night
install segovia-night/segovia-night.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Segovia_Night
#
# Theme 67/80
#
# Make 'Shapy' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Shapy
# Install 'Shapy' theme files
install shapy/background.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Shapy
install shapy/config.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Shapy
install shapy/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Shapy
install shapy/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Shapy
install shapy/option.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Shapy
install shapy/README $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Shapy
install shapy/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Shapy
install shapy/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Shapy
install shapy/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Shapy
#
# Theme 68/80
#
# Make 'Simple-Gnome-Logo' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Simple-Gnome-Logo
# Install 'Simple-Gnome-Logo' theme files
install Gnome-Logo/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Simple-Gnome-Logo
install Gnome-Logo/gnome-foot-black.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Simple-Gnome-Logo
install Gnome-Logo/Gnome-Logo.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Simple-Gnome-Logo
install Gnome-Logo/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Simple-Gnome-Logo
#
# Theme 69/80
#
# Make 'Space' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Space
# Install 'Space' theme files
install Space/background.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Space
install Space/ball.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Space
install Space/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Space
install Space/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Space
install Space/option.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Space
install Space/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Space
install Space/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Space
install Space/space.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Space
install Space/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Space

#
# Theme 71/80
#
# Make 'SpreadFirefox' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/SpreadFirefox
# Install 'SpreadFirefox' theme files
install SpreadFirefox/firefox.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/SpreadFirefox
install SpreadFirefox/firefox.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/SpreadFirefox
install SpreadFirefox/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/SpreadFirefox
install SpreadFirefox/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/SpreadFirefox
install SpreadFirefox/screenshot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/SpreadFirefox
#
# Theme 72/80
#
# Make 'STGO' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/STGO
# Install 'STGO' theme files
install stgo/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/STGO
install stgo/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/STGO
install stgo/stgo1.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/STGO
install stgo/stgo2.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/STGO
install stgo/stgo3.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/STGO
install stgo/stgo4.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/STGO
install stgo/stgo.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/STGO
install stgo/stgo.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/STGO
#
# Theme 73/80
#
# Make 'Stop_TCPA' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Stop_TCPA
# Install 'Stop_TCPA' theme files
install tcpa/background.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Stop_TCPA
install tcpa/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Stop_TCPA
install tcpa/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Stop_TCPA
install tcpa/option.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Stop_TCPA
install tcpa/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Stop_TCPA
install tcpa/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Stop_TCPA
install tcpa/tcpa.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Stop_TCPA
#
# Theme 74/80
#
# Make 'SVG_Sakura' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/SVG_Sakura
# Install 'SVG_Sakura' theme files
install sakura/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/SVG_Sakura
install sakura/gdm_shot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/SVG_Sakura
install sakura/options_color.svg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/SVG_Sakura
install sakura/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/SVG_Sakura
install sakura/options.svg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/SVG_Sakura
install sakura/readme $RPM_BUILD_ROOT%{_datadir}/gdm/themes/SVG_Sakura
install sakura/sakura.svg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/SVG_Sakura
install sakura/sakura.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/SVG_Sakura
#
# Theme 75/80
#
# Make 'Synergy' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Synergy
# Install 'Synergy' theme files
install Synergy/background.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Synergy
install Synergy/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Synergy
install Synergy/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Synergy
install Synergy/halt.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Synergy
install Synergy/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Synergy
install Synergy/reboot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Synergy
install Synergy/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Synergy
install Synergy/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Synergy
install Synergy/theme.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Synergy
#
# Theme 76/80
#
# Make 'Taipei' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Taipei
# Install 'Taipei' theme files
install Taipei/background.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Taipei
install Taipei/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Taipei
install Taipei/help.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Taipei
install Taipei/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Taipei
install Taipei/Taipei.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Taipei
install Taipei/theme.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Taipei
#
# Theme 77/80
#
# Make 'The_Dark_Crystal' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/The_Dark_Crystal
# Install 'The_Dark_Crystal' theme files
install darkcrystal/background.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/The_Dark_Crystal
install darkcrystal/darkcrystal.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/The_Dark_Crystal
install darkcrystal/disconnect.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/The_Dark_Crystal
install darkcrystal/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/The_Dark_Crystal
install darkcrystal/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/The_Dark_Crystal
install darkcrystal/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/The_Dark_Crystal
install darkcrystal/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/The_Dark_Crystal
#
# Theme 78/80
#
# Make 'Todmorden' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Todmorden
# Install 'Todmorden' theme files
install Todmorden/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Todmorden
install Todmorden/help.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Todmorden
install Todmorden/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Todmorden
install Todmorden/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Todmorden
install Todmorden/todmorden.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Todmorden
install Todmorden/todmorden.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Todmorden
#
# Theme 79/80
#
# Make 'Valladolid' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Valladolid
# Install 'Valladolid' theme files
install valladolid/ava-desconectar.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Valladolid
install valladolid/ava-opcion.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Valladolid
install valladolid/ava-sesion.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Valladolid
install valladolid/ava-sistema.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Valladolid
install valladolid/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Valladolid
install valladolid/screenshot.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Valladolid
install valladolid/valladolid.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Valladolid
install valladolid/valladolid.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/Valladolid
#
# Theme 80/80
#
# Make 'XPTO' theme directory
install -d $RPM_BUILD_ROOT%{_datadir}/gdm/themes/XPTO
# Install 'XPTO' theme files
install xpto/GdmGreeterTheme.desktop $RPM_BUILD_ROOT%{_datadir}/gdm/themes/XPTO
install xpto/language.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/XPTO
install xpto/options.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/XPTO
install xpto/quit.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/XPTO
install xpto/session.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/XPTO
install xpto/system.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/XPTO
install xpto/xpto_bg.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/XPTO
install xpto/xpto.jpg $RPM_BUILD_ROOT%{_datadir}/gdm/themes/XPTO
install xpto/xpto_shot.png $RPM_BUILD_ROOT%{_datadir}/gdm/themes/XPTO
install xpto/xpto.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/XPTO
install xpto/xpt.xml $RPM_BUILD_ROOT%{_datadir}/gdm/themes/XPTO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes
%doc README

#
# Theme 00/80
#
%files 300-lantueno
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/300-lantueno
%{_datadir}/gdm/themes/300-lantueno/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/300-lantueno/language.png
%{_datadir}/gdm/themes/300-lantueno/lantueno.png
%{_datadir}/gdm/themes/300-lantueno/lantueno.xml
%{_datadir}/gdm/themes/300-lantueno/options.png
%{_datadir}/gdm/themes/300-lantueno/quit.png
%{_datadir}/gdm/themes/300-lantueno/screenshot.jpg
%{_datadir}/gdm/themes/300-lantueno/session.png
%{_datadir}/gdm/themes/300-lantueno/system.png

#
# Theme 01/80
#
%files 9nome-Darmis
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/9nome-Darmis
%{_datadir}/gdm/themes/9nome-Darmis/background.png
%{_datadir}/gdm/themes/9nome-Darmis/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/9nome-Darmis/gdm-theme.xml
%{_datadir}/gdm/themes/9nome-Darmis/halt.png
%{_datadir}/gdm/themes/9nome-Darmis/language.png
%{_datadir}/gdm/themes/9nome-Darmis/quit.png
%{_datadir}/gdm/themes/9nome-Darmis/reboot.png
%{_datadir}/gdm/themes/9nome-Darmis/screenshot.png
%{_datadir}/gdm/themes/9nome-Darmis/session.png

#
# Theme 02/80
#
%files Angel
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Angel
%{_datadir}/gdm/themes/Angel/angel.png
%{_datadir}/gdm/themes/Angel/angel.xml
%{_datadir}/gdm/themes/Angel/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Angel/language.png
%{_datadir}/gdm/themes/Angel/options.png
%{_datadir}/gdm/themes/Angel/quit.png
%{_datadir}/gdm/themes/Angel/screenshot.png
%{_datadir}/gdm/themes/Angel/session.png
%{_datadir}/gdm/themes/Angel/system.png

#
# Theme 04/80
#
%files Bee_at_Work
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Bee_at_Work
%{_datadir}/gdm/themes/Bee_at_Work/background.jpg
%{_datadir}/gdm/themes/Bee_at_Work/BeeAtWork.jpg
%{_datadir}/gdm/themes/Bee_at_Work/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Bee_at_Work/help.png
%{_datadir}/gdm/themes/Bee_at_Work/options.png
%{_datadir}/gdm/themes/Bee_at_Work/theme.xml

#
# Theme 05/80
#
%files Bijou
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Bijou
%{_datadir}/gdm/themes/Bijou/background.png
%{_datadir}/gdm/themes/Bijou/bijou.xml
%{_datadir}/gdm/themes/Bijou/disconnect.png
%{_datadir}/gdm/themes/Bijou/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Bijou/language.png
%{_datadir}/gdm/themes/Bijou/screenshot.png
%{_datadir}/gdm/themes/Bijou/session.png
%{_datadir}/gdm/themes/Bijou/system.png

#
# Theme 06/80
#
%files Blueish
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Blueish
%{_datadir}/gdm/themes/Blueish/bluish-gdm.xml
%{_datadir}/gdm/themes/Blueish/bluish.png
%{_datadir}/gdm/themes/Blueish/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Blueish/help.png
%{_datadir}/gdm/themes/Blueish/language.png
%{_datadir}/gdm/themes/Blueish/options.png
%{_datadir}/gdm/themes/Blueish/quit.png
%{_datadir}/gdm/themes/Blueish/screenshot.png
%{_datadir}/gdm/themes/Blueish/system.png

#
# Theme 07/80
#
%files Butterfly
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Butterfly
%{_datadir}/gdm/themes/Butterfly/bfly.jpg
%{_datadir}/gdm/themes/Butterfly/butterfly.jpg
%{_datadir}/gdm/themes/Butterfly/butterfly_tahoma.xml
%{_datadir}/gdm/themes/Butterfly/butterfly.xml
%{_datadir}/gdm/themes/Butterfly/disconnect.png
%{_datadir}/gdm/themes/Butterfly/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Butterfly/option.png
%{_datadir}/gdm/themes/Butterfly/session.png
%{_datadir}/gdm/themes/Butterfly/system.png

#
# Theme 08/80
#
%files Colorado_Windmill
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Colorado_Windmill
%{_datadir}/gdm/themes/Colorado_Windmill/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Colorado_Windmill/language.png
%{_datadir}/gdm/themes/Colorado_Windmill/options.png
%{_datadir}/gdm/themes/Colorado_Windmill/quit.png
%{_datadir}/gdm/themes/Colorado_Windmill/session.png
%{_datadir}/gdm/themes/Colorado_Windmill/system.png
%{_datadir}/gdm/themes/Colorado_Windmill/windmill.jpg
%{_datadir}/gdm/themes/Colorado_Windmill/windmill-screenshot.jpg
%{_datadir}/gdm/themes/Colorado_Windmill/Windmill.xml

#
# Theme 09/80
#
%files Cracked_Windows
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Cracked_Windows
%{_datadir}/gdm/themes/Cracked_Windows/cracked-windows.jpg
%{_datadir}/gdm/themes/Cracked_Windows/cracked-windows.xml
%{_datadir}/gdm/themes/Cracked_Windows/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Cracked_Windows/language.png
%{_datadir}/gdm/themes/Cracked_Windows/quit.png
%{_datadir}/gdm/themes/Cracked_Windows/screenshot.jpg
%{_datadir}/gdm/themes/Cracked_Windows/session.png
%{_datadir}/gdm/themes/Cracked_Windows/system.png

#
# Theme 10/80
#
%files Crop_Circles
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Crop_Circles
%{_datadir}/gdm/themes/Crop_Circles/background.jpg
%{_datadir}/gdm/themes/Crop_Circles/Bottombar.svg
%{_datadir}/gdm/themes/Crop_Circles/disconnect.png
%{_datadir}/gdm/themes/Crop_Circles/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Crop_Circles/gnome-logo.png
%{_datadir}/gdm/themes/Crop_Circles/halt.png
%{_datadir}/gdm/themes/Crop_Circles/lang.png
%{_datadir}/gdm/themes/Crop_Circles/List.svg
%{_datadir}/gdm/themes/Crop_Circles/Login.svg
%{_datadir}/gdm/themes/Crop_Circles/options.png
%{_datadir}/gdm/themes/Crop_Circles/readme
%{_datadir}/gdm/themes/Crop_Circles/reboot.png
%{_datadir}/gdm/themes/Crop_Circles/roundrect.svg
%{_datadir}/gdm/themes/Crop_Circles/screenshot.png
%{_datadir}/gdm/themes/Crop_Circles/session.png
%{_datadir}/gdm/themes/Crop_Circles/signs.xml
%{_datadir}/gdm/themes/Crop_Circles/system.png
%{_datadir}/gdm/themes/Crop_Circles/Topbar.svg

#
# Theme 11/80
#
%files Crystal
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Crystal
%{_datadir}/gdm/themes/Crystal/background.jpg
%{_datadir}/gdm/themes/Crystal/Crystal.xml
%{_datadir}/gdm/themes/Crystal/disconnect.png
%{_datadir}/gdm/themes/Crystal/galikynes.jpg
%{_datadir}/gdm/themes/Crystal/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Crystal/option.png
%{_datadir}/gdm/themes/Crystal/screenshot.png
%{_datadir}/gdm/themes/Crystal/session.png
%{_datadir}/gdm/themes/Crystal/system.png

#
# Theme 12/80
#
%files Crystal_For_Gnome
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Crystal_For_Gnome
%{_datadir}/gdm/themes/Crystal_For_Gnome/Acknowlagements
%{_datadir}/gdm/themes/Crystal_For_Gnome/background.png
%{_datadir}/gdm/themes/Crystal_For_Gnome/Crystal_for_Gnome.xml
%{_datadir}/gdm/themes/Crystal_For_Gnome/disconnect.png
%{_datadir}/gdm/themes/Crystal_For_Gnome/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Crystal_For_Gnome/halt.png
%{_datadir}/gdm/themes/Crystal_For_Gnome/options.png
%{_datadir}/gdm/themes/Crystal_For_Gnome/reboot.png
%{_datadir}/gdm/themes/Crystal_For_Gnome/screenshot.png
%{_datadir}/gdm/themes/Crystal_For_Gnome/session.png
%{_datadir}/gdm/themes/Crystal_For_Gnome/system.png

#
# Theme 13/80
#
%files Crystal_for_Gnome_-_theme_2
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2
%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2/disconnect.png
%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2/gentoo.png
%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2/language.png
%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2/loginbox.png
%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2/screenshot.png
%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2/session.png
%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2/theme.xml
%{_datadir}/gdm/themes/Crystal_for_Gnome_-_theme_2/wall.svg

#
# Theme 14/80
#
%files Crystal_Rose
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Crystal_Rose
%{_datadir}/gdm/themes/Crystal_Rose/crystal-rose.jpg
%{_datadir}/gdm/themes/Crystal_Rose/crystal-rose.png
%{_datadir}/gdm/themes/Crystal_Rose/crystal-rose-screenshot.png
%{_datadir}/gdm/themes/Crystal_Rose/crystal-rose.xml
%{_datadir}/gdm/themes/Crystal_Rose/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Crystal_Rose/options.png
%{_datadir}/gdm/themes/Crystal_Rose/crystal-rose.png

#
# Theme 15/80
#
%files Cubic_Linux_and_Gnome
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Cubic_Linux_and_Gnome
%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/background.jpg
%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/disconnect.png
%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/halt.png
%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/options.png
%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/reboot.png
%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/screenshot.jpg
%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/session.png
%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/theme.xml

#
# Theme 16/80
#
%files Dart_Frog
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Dart_Frog
%{_datadir}/gdm/themes/Dart_Frog/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Dart_Frog/language.png
%{_datadir}/gdm/themes/Dart_Frog/options.png
%{_datadir}/gdm/themes/Dart_Frog/pitcherplant.png
%{_datadir}/gdm/themes/Dart_Frog/pitcherplant.xml
%{_datadir}/gdm/themes/Dart_Frog/quit.png
%{_datadir}/gdm/themes/Dart_Frog/screenshot.png
%{_datadir}/gdm/themes/Dart_Frog/session.png
%{_datadir}/gdm/themes/Dart_Frog/system.png

#
# Theme 17/80
#
%files Dawn
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Dawn
%{_datadir}/gdm/themes/Dawn/background.jpg
%{_datadir}/gdm/themes/Dawn/dawn.xml
%{_datadir}/gdm/themes/Dawn/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Dawn/option.png
%{_datadir}/gdm/themes/Dawn/quit.png
%{_datadir}/gdm/themes/Dawn/screenshot.jpg
%{_datadir}/gdm/themes/Dawn/session.png
%{_datadir}/gdm/themes/Dawn/system.png

#
# Theme 18/80
#
%files Daybreak
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Daybreak
%{_datadir}/gdm/themes/Daybreak/daybreak.png
%{_datadir}/gdm/themes/Daybreak/daybreak.xml
%{_datadir}/gdm/themes/Daybreak/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Daybreak/language.png
%{_datadir}/gdm/themes/Daybreak/options.png
%{_datadir}/gdm/themes/Daybreak/quit.png
%{_datadir}/gdm/themes/Daybreak/screenshot.png
%{_datadir}/gdm/themes/Daybreak/session.png
%{_datadir}/gdm/themes/Daybreak/system.png

#
# Theme 19/80
#
%files Delicious
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Delicious
%{_datadir}/gdm/themes/Delicious/delicious.xml
%{_datadir}/gdm/themes/Delicious/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Delicious/head1.png
%{_datadir}/gdm/themes/Delicious/mampf.png
%{_datadir}/gdm/themes/Delicious/screenshot.jpg
%{_datadir}/gdm/themes/Delicious/screenshot-small.png
%{_datadir}/gdm/themes/Delicious/sys.png

#
# Theme 20/80
#
%files Devils_Candy
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Devils_Candy
%{_datadir}/gdm/themes/Devils_Candy/background.jpg
%{_datadir}/gdm/themes/Devils_Candy/ball.png
%{_datadir}/gdm/themes/Devils_Candy/devil.xml
%{_datadir}/gdm/themes/Devils_Candy/disconnect.png
%{_datadir}/gdm/themes/Devils_Candy/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Devils_Candy/option.png
%{_datadir}/gdm/themes/Devils_Candy/screenshot.jpg
%{_datadir}/gdm/themes/Devils_Candy/session.png
%{_datadir}/gdm/themes/Devils_Candy/system.png

#
# Theme 21/80
#
%files Dreaming_Alien
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Dreaming_Alien
%{_datadir}/gdm/themes/Dreaming_Alien/background.png
%{_datadir}/gdm/themes/Dreaming_Alien/disconnect.png
%{_datadir}/gdm/themes/Dreaming_Alien/dreaming-alien.xml
%{_datadir}/gdm/themes/Dreaming_Alien/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Dreaming_Alien/language.png
%{_datadir}/gdm/themes/Dreaming_Alien/screenshot.png
%{_datadir}/gdm/themes/Dreaming_Alien/session.png
%{_datadir}/gdm/themes/Dreaming_Alien/system.png

#
# Theme 22/80
#
%files DumbCloud
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/DumbCloud
%{_datadir}/gdm/themes/DumbCloud/cloud2.png
%{_datadir}/gdm/themes/DumbCloud/dumbcloud.svg
%{_datadir}/gdm/themes/DumbCloud/dumbcloud.xml
%{_datadir}/gdm/themes/DumbCloud/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/DumbCloud/help.png
%{_datadir}/gdm/themes/DumbCloud/options.png
%{_datadir}/gdm/themes/DumbCloud/test2.svg

#
# Theme 23/80
#
%files Emo-Blue
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Emo-Blue
%{_datadir}/gdm/themes/Emo-Blue/emo-blue.jpg
%{_datadir}/gdm/themes/Emo-Blue/emo-blue.xml
%{_datadir}/gdm/themes/Emo-Blue/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Emo-Blue/language.png
%{_datadir}/gdm/themes/Emo-Blue/options.png
%{_datadir}/gdm/themes/Emo-Blue/quit.png
%{_datadir}/gdm/themes/Emo-Blue/screenshot.jpg
%{_datadir}/gdm/themes/Emo-Blue/session.png
%{_datadir}/gdm/themes/Emo-Blue/system.png

#
# Theme 24/80
#
%files Falling_Angel
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Falling_Angel
%{_datadir}/gdm/themes/Falling_Angel/falling-angel.jpg
%{_datadir}/gdm/themes/Falling_Angel/falling-angel-shot.png
%{_datadir}/gdm/themes/Falling_Angel/falling-angel.xml
%{_datadir}/gdm/themes/Falling_Angel/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Falling_Angel/language.png
%{_datadir}/gdm/themes/Falling_Angel/options.png
%{_datadir}/gdm/themes/Falling_Angel/quit.png
%{_datadir}/gdm/themes/Falling_Angel/session.png
%{_datadir}/gdm/themes/Falling_Angel/system.png

#
# Theme 25/80
#
%files Fire_Breathing_Robot
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Fire_Breathing_Robot
%{_datadir}/gdm/themes/Fire_Breathing_Robot/flames.png
%{_datadir}/gdm/themes/Fire_Breathing_Robot/flame.xml
%{_datadir}/gdm/themes/Fire_Breathing_Robot/gdmbar.png
%{_datadir}/gdm/themes/Fire_Breathing_Robot/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Fire_Breathing_Robot/options.png
%{_datadir}/gdm/themes/Fire_Breathing_Robot/screenshot.png
%{_datadir}/gdm/themes/Fire_Breathing_Robot/shadow-bl.png
%{_datadir}/gdm/themes/Fire_Breathing_Robot/shadow-b.png
%{_datadir}/gdm/themes/Fire_Breathing_Robot/shadow-br.png
%{_datadir}/gdm/themes/Fire_Breathing_Robot/shadow-l.png
%{_datadir}/gdm/themes/Fire_Breathing_Robot/shadow-r.png
%{_datadir}/gdm/themes/Fire_Breathing_Robot/shadow-tl.png
%{_datadir}/gdm/themes/Fire_Breathing_Robot/shadow-t.png
%{_datadir}/gdm/themes/Fire_Breathing_Robot/shadow-tr.png

#
# Theme 26/80
#
%files Flowers
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Flowers
%{_datadir}/gdm/themes/Flowers/background.jpg
%{_datadir}/gdm/themes/Flowers/flowers.xml
%{_datadir}/gdm/themes/Flowers/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Flowers/help.png
%{_datadir}/gdm/themes/Flowers/options.png
%{_datadir}/gdm/themes/Flowers/screenshot.jpg
%{_datadir}/gdm/themes/Flowers/system.png

#
# Theme 27/80
#
%files gcr-ddlm
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/gcr-ddlm
%{_datadir}/gdm/themes/gcr-ddlm/gcr-ddlm.background.png
%{_datadir}/gdm/themes/gcr-ddlm/gcr-ddlm.background.screenshot.png
%{_datadir}/gdm/themes/gcr-ddlm/gcr-ddlm.xml
%{_datadir}/gdm/themes/gcr-ddlm/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/gcr-ddlm/language.png
%{_datadir}/gdm/themes/gcr-ddlm/quit.png
%{_datadir}/gdm/themes/gcr-ddlm/session.png
%{_datadir}/gdm/themes/gcr-ddlm/system.png

#
# Theme 28/80
#
%files Gdm_Dropline
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Gdm_Dropline
%{_datadir}/gdm/themes/Gdm_Dropline/dropline-blue.png
%{_datadir}/gdm/themes/Gdm_Dropline/dropline-blue.xml
%{_datadir}/gdm/themes/Gdm_Dropline/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Gdm_Dropline/language.png
%{_datadir}/gdm/themes/Gdm_Dropline/options.png
%{_datadir}/gdm/themes/Gdm_Dropline/quit.png
%{_datadir}/gdm/themes/Gdm_Dropline/screenshot.png
%{_datadir}/gdm/themes/Gdm_Dropline/session.png
%{_datadir}/gdm/themes/Gdm_Dropline/system.png

#
# Theme 29/80
#
%files GDM_Waves
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/GDM_Waves
%{_datadir}/gdm/themes/GDM_Waves/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/GDM_Waves/gdm-waves.png
%{_datadir}/gdm/themes/GDM_Waves/gdm-waves-screenshot.png
%{_datadir}/gdm/themes/GDM_Waves/gdm-waves.xml
%{_datadir}/gdm/themes/GDM_Waves/language.png
%{_datadir}/gdm/themes/GDM_Waves/options.png
%{_datadir}/gdm/themes/GDM_Waves/quit.png
%{_datadir}/gdm/themes/GDM_Waves/session.png
%{_datadir}/gdm/themes/GDM_Waves/system.png

#
# Theme 30/80
#
%files GDM-GlassFoot
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/GDM-GlassFoot
%{_datadir}/gdm/themes/GDM-GlassFoot/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/GDM-GlassFoot/glass.png
%{_datadir}/gdm/themes/GDM-GlassFoot/GNOME-GlassFoot.xml
%{_datadir}/gdm/themes/GDM-GlassFoot/language.png
%{_datadir}/gdm/themes/GDM-GlassFoot/quit.png
%{_datadir}/gdm/themes/GDM-GlassFoot/screenshot.png
%{_datadir}/gdm/themes/GDM-GlassFoot/session.png
%{_datadir}/gdm/themes/GDM-GlassFoot/system.png

#
# Theme 31/80
#
%files GDM-Mosaic
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/GDM-Mosaic
%{_datadir}/gdm/themes/GDM-Mosaic/disconnect.png
%{_datadir}/gdm/themes/GDM-Mosaic/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/GDM-Mosaic/Mosaic.png
%{_datadir}/gdm/themes/GDM-Mosaic/Mosaic.xml
%{_datadir}/gdm/themes/GDM-Mosaic/option.png
%{_datadir}/gdm/themes/GDM-Mosaic/screenshot.jpg
%{_datadir}/gdm/themes/GDM-Mosaic/session.png
%{_datadir}/gdm/themes/GDM-Mosaic/system.png

#
# Theme 32/80
#
%files Glassy
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Glassy
%{_datadir}/gdm/themes/Glassy/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Glassy/glassy.png
%{_datadir}/gdm/themes/Glassy/glassy.xml
%{_datadir}/gdm/themes/Glassy/help.png
%{_datadir}/gdm/themes/Glassy/language.png
%{_datadir}/gdm/themes/Glassy/options.png
%{_datadir}/gdm/themes/Glassy/quit.png
%{_datadir}/gdm/themes/Glassy/screenshot.png
%{_datadir}/gdm/themes/Glassy/system.png

#
# Theme 33/80
#
%files Gnome_Chile
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Gnome_Chile
%{_datadir}/gdm/themes/Gnome_Chile/fondo.png
%{_datadir}/gdm/themes/Gnome_Chile/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Gnome_Chile/gnome-chile.xml
%{_datadir}/gdm/themes/Gnome_Chile/language.png
%{_datadir}/gdm/themes/Gnome_Chile/options.png
%{_datadir}/gdm/themes/Gnome_Chile/quit.png
%{_datadir}/gdm/themes/Gnome_Chile/screenshot.png
%{_datadir}/gdm/themes/Gnome_Chile/session.png
%{_datadir}/gdm/themes/Gnome_Chile/system.png

#
# Theme 34/80
#
%files Gnome_Plain_Swoosh_GDM_Theme
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme/background.png
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme/curve-bottom_left.png
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme/curve-bottom_right.png
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme/curve-top_left.png
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme/curve-top_right.png
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme/options1.png
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme/options2.png
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme/options_hilite1.png
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme/options_hilite2.png
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme/screenshot.png
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme/swoosh.xml

#
# Theme 35/80
#
%files Gnome_Plain_Swoosh_GDM_Theme_TNG
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG/background.png
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG/dashed-rect.svg
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG/dotline.png
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG/gnome-linux-desktop.png
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG/plain-swoosh-tng.xml
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG/README
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG/screenshot.png
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG/shade-left.png
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG/shade-right.png
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG/small-n.png
%{_datadir}/gdm/themes/Gnome_Plain_Swoosh_GDM_Theme_TNG/vline.svg

#
# Theme 36/80
#
%files Hantzley
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Hantzley
%{_datadir}/gdm/themes/Hantzley/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Hantzley/hantzley.png
%{_datadir}/gdm/themes/Hantzley/hantzley.xml
%{_datadir}/gdm/themes/Hantzley/language.png
%{_datadir}/gdm/themes/Hantzley/options.png
%{_datadir}/gdm/themes/Hantzley/quit.png
%{_datadir}/gdm/themes/Hantzley/screenshot.png
%{_datadir}/gdm/themes/Hantzley/session.png
%{_datadir}/gdm/themes/Hantzley/system.png

#
# Theme 37/80
#
%files Hunter
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Hunter
%{_datadir}/gdm/themes/Hunter/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Hunter/help.png
%{_datadir}/gdm/themes/Hunter/hunter.png
%{_datadir}/gdm/themes/Hunter/hunter.xml
%{_datadir}/gdm/themes/Hunter/options.png
%{_datadir}/gdm/themes/Hunter/screenshot.png

#
# Theme 38/80
#
%files hybridFUSION
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/hybridFUSION
%{_datadir}/gdm/themes/hybridFUSION/ConVerSion_version_Two.png
%{_datadir}/gdm/themes/hybridFUSION/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/hybridFUSION/hybridFUSION.xml
%{_datadir}/gdm/themes/hybridFUSION/options.png
%{_datadir}/gdm/themes/hybridFUSION/screenshot.png
%{_datadir}/gdm/themes/hybridFUSION/shadow-bl.png
%{_datadir}/gdm/themes/hybridFUSION/shadow-b.png
%{_datadir}/gdm/themes/hybridFUSION/shadow-br.png
%{_datadir}/gdm/themes/hybridFUSION/shadow-l.png
%{_datadir}/gdm/themes/hybridFUSION/shadow-r.png
%{_datadir}/gdm/themes/hybridFUSION/shadow-tl.png
%{_datadir}/gdm/themes/hybridFUSION/shadow-t.png
%{_datadir}/gdm/themes/hybridFUSION/shadow-tr.png
%{_datadir}/gdm/themes/hybridFUSION/skowals.png

#
# Theme 39/80
#
%files In_This_World
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/In_This_World
%{_datadir}/gdm/themes/In_This_World/background.png
%{_datadir}/gdm/themes/In_This_World/disconnect.png
%{_datadir}/gdm/themes/In_This_World/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/In_This_World/InThisWorld.xml
%{_datadir}/gdm/themes/In_This_World/option.png
%{_datadir}/gdm/themes/In_This_World/screenshot.jpg
%{_datadir}/gdm/themes/In_This_World/session.png
%{_datadir}/gdm/themes/In_This_World/system.png

#
# Theme 40/80
#
%files KDE_Crystal
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/KDE_Crystal
%{_datadir}/gdm/themes/KDE_Crystal/background.png
%{_datadir}/gdm/themes/KDE_Crystal/crystal.xml
%{_datadir}/gdm/themes/KDE_Crystal/disconnect.png
%{_datadir}/gdm/themes/KDE_Crystal/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/KDE_Crystal/halt.png
%{_datadir}/gdm/themes/KDE_Crystal/options.png
%{_datadir}/gdm/themes/KDE_Crystal/reboot.png
%{_datadir}/gdm/themes/KDE_Crystal/screenshot.png
%{_datadir}/gdm/themes/KDE_Crystal/session.png

#
# Theme 41/80
#
%files Kinkakuji
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Kinkakuji
%{_datadir}/gdm/themes/Kinkakuji/background.jpg
%{_datadir}/gdm/themes/Kinkakuji/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Kinkakuji/help.png
%{_datadir}/gdm/themes/Kinkakuji/options.png
%{_datadir}/gdm/themes/Kinkakuji/screenshot.jpg
%{_datadir}/gdm/themes/Kinkakuji/theme.xml

#
# Theme 42/80
#
%files Knoke
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Knoke
%{_datadir}/gdm/themes/Knoke/back.jpg
%{_datadir}/gdm/themes/Knoke/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Knoke/knoke.jpg
%{_datadir}/gdm/themes/Knoke/knoke.xml
%{_datadir}/gdm/themes/Knoke/language.png
%{_datadir}/gdm/themes/Knoke/options.png
%{_datadir}/gdm/themes/Knoke/quit.png
%{_datadir}/gdm/themes/Knoke/session.png
%{_datadir}/gdm/themes/Knoke/system.png

#
# Theme 43/80
#
%files La_Bisbal_dEmpord_nevada
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada
%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/labisbal-desconectar.jpg
%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/labisbal.jpg
%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/labisbal-opcions.jpg
%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/labisbal-sessio.jpg
%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/labisbal-sistema.jpg
%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/labisbal.xml
%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/screenshot.jpg

#
# Theme 44/80
#
%files Leon
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Leon
%{_datadir}/gdm/themes/Leon/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Leon/leon-desconectar.jpg
%{_datadir}/gdm/themes/Leon/leon.jpg
%{_datadir}/gdm/themes/Leon/leon-opciones.jpg
%{_datadir}/gdm/themes/Leon/leon-sesion.jpg
%{_datadir}/gdm/themes/Leon/leon-sistema.jpg
%{_datadir}/gdm/themes/Leon/leon.xml
%{_datadir}/gdm/themes/Leon/screenshot.jpg

#
# Theme 45/80
#
%files Linux_Crystal
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Linux_Crystal
%{_datadir}/gdm/themes/Linux_Crystal/background.png
%{_datadir}/gdm/themes/Linux_Crystal/disconnect.png
%{_datadir}/gdm/themes/Linux_Crystal/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Linux_Crystal/halt.png
%{_datadir}/gdm/themes/Linux_Crystal/Linux_Crystal.xml
%{_datadir}/gdm/themes/Linux_Crystal/options.png
%{_datadir}/gdm/themes/Linux_Crystal/reboot.png
%{_datadir}/gdm/themes/Linux_Crystal/screenshot.png
%{_datadir}/gdm/themes/Linux_Crystal/session.png
%{_datadir}/gdm/themes/Linux_Crystal/system.png

#
# Theme 46/80
#
%files LinuxTux
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/LinuxTux
%{_datadir}/gdm/themes/LinuxTux/background.jpg
%{_datadir}/gdm/themes/LinuxTux/disconnect.png
%{_datadir}/gdm/themes/LinuxTux/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/LinuxTux/option.png
%{_datadir}/gdm/themes/LinuxTux/screenshot.png
%{_datadir}/gdm/themes/LinuxTux/session.png
%{_datadir}/gdm/themes/LinuxTux/system.png
%{_datadir}/gdm/themes/LinuxTux/tux.png
%{_datadir}/gdm/themes/LinuxTux/tux.xml

#
# Theme 47/80
#
%files Luna_GDM_Theme
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Luna_GDM_Theme

#
# Theme 48/80
#
%files M-83
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/M-83
%{_datadir}/gdm/themes/M-83/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/M-83/options.png
%{_datadir}/gdm/themes/M-83/space.png
%{_datadir}/gdm/themes/M-83/Space.xml
%{_datadir}/gdm/themes/M-83/ss.png

#
# Theme 49/80
#
%files Machu_Picchu
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Machu_Picchu
%{_datadir}/gdm/themes/Machu_Picchu/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Machu_Picchu/Machu?Picchu.xml
%{_datadir}/gdm/themes/Machu_Picchu/MP-ledge-bg.png
%{_datadir}/gdm/themes/Machu_Picchu/MP-tall-options.png
%{_datadir}/gdm/themes/Machu_Picchu/MP-tall-quit.png
%{_datadir}/gdm/themes/Machu_Picchu/MP-tall-session.png
%{_datadir}/gdm/themes/Machu_Picchu/MP-tall-system.png
%{_datadir}/gdm/themes/Machu_Picchu/screenshot.png

#
# Theme 50/80
#
%files ManzanaTux
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/ManzanaTux
%{_datadir}/gdm/themes/ManzanaTux/disconnect.png
%{_datadir}/gdm/themes/ManzanaTux/galikynes.jpg
%{_datadir}/gdm/themes/ManzanaTux/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/ManzanaTux/ManzanaTux.xml
%{_datadir}/gdm/themes/ManzanaTux/option.png
%{_datadir}/gdm/themes/ManzanaTux/screenshot.png
%{_datadir}/gdm/themes/ManzanaTux/session.png
%{_datadir}/gdm/themes/ManzanaTux/system.png
%{_datadir}/gdm/themes/ManzanaTux/thinkshell.jpg

#
# Theme 51/80
#
%files ManzanaTuxBlack
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/ManzanaTuxBlack
%{_datadir}/gdm/themes/ManzanaTuxBlack/disconnect.png
%{_datadir}/gdm/themes/ManzanaTuxBlack/galikynes.jpg
%{_datadir}/gdm/themes/ManzanaTuxBlack/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/ManzanaTuxBlack/ManzanaTuxBlack.xml
%{_datadir}/gdm/themes/ManzanaTuxBlack/option.png
%{_datadir}/gdm/themes/ManzanaTuxBlack/screenshot.png
%{_datadir}/gdm/themes/ManzanaTuxBlack/session.png
%{_datadir}/gdm/themes/ManzanaTuxBlack/system.png
%{_datadir}/gdm/themes/ManzanaTuxBlack/thinklinux.jpg

#
# Theme 52/80
#
%files Milk
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Milk
%{_datadir}/gdm/themes/Milk/background.png
%{_datadir}/gdm/themes/Milk/background.svg
%{_datadir}/gdm/themes/Milk/disconnect.png
%{_datadir}/gdm/themes/Milk/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Milk/gnome-logo.png
%{_datadir}/gdm/themes/Milk/milk.xml
%{_datadir}/gdm/themes/Milk/options.png
%{_datadir}/gdm/themes/Milk/screenshot.png
%{_datadir}/gdm/themes/Milk/session.png
%{_datadir}/gdm/themes/Milk/system.png

#
# Theme 53/80
#
%files Mirrored
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Mirrored
%{_datadir}/gdm/themes/Mirrored/background.png
%{_datadir}/gdm/themes/Mirrored/COPYING
%{_datadir}/gdm/themes/Mirrored/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Mirrored/head1.png
%{_datadir}/gdm/themes/Mirrored/head3.png
%{_datadir}/gdm/themes/Mirrored/head4.png
%{_datadir}/gdm/themes/Mirrored/head5.png
%{_datadir}/gdm/themes/Mirrored/mirrored.xml
%{_datadir}/gdm/themes/Mirrored/screenshot.jpg
%{_datadir}/gdm/themes/Mirrored/sys.png

#
# Theme 54/80
#
%files Mono_Metal
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Mono_Metal
%{_datadir}/gdm/themes/Mono_Metal/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Mono_Metal/language.png
%{_datadir}/gdm/themes/Mono_Metal/metal.png
%{_datadir}/gdm/themes/Mono_Metal/mono_metal.xml
%{_datadir}/gdm/themes/Mono_Metal/quit.png
%{_datadir}/gdm/themes/Mono_Metal/screenshot.png
%{_datadir}/gdm/themes/Mono_Metal/session.png
%{_datadir}/gdm/themes/Mono_Metal/system.png

#
# Theme 55/80
#
%files Morning_Light
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Morning_Light
%{_datadir}/gdm/themes/Morning_Light/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Morning_Light/help.png
%{_datadir}/gdm/themes/Morning_Light/morning.jpg
%{_datadir}/gdm/themes/Morning_Light/options.png
%{_datadir}/gdm/themes/Morning_Light/screenshot.png
%{_datadir}/gdm/themes/Morning_Light/theme.xml

#
# Theme 56/80
#
%files Mozi
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Mozi
%{_datadir}/gdm/themes/Mozi/disconnect.png
%{_datadir}/gdm/themes/Mozi/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Mozi/mozilla.jpg
%{_datadir}/gdm/themes/Mozi/option.png
%{_datadir}/gdm/themes/Mozi/screenshot.png
%{_datadir}/gdm/themes/Mozi/session.png
%{_datadir}/gdm/themes/Mozi/soho.xml
%{_datadir}/gdm/themes/Mozi/system.png

#
# Theme 57/80
#
%files Murcia
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Murcia
%{_datadir}/gdm/themes/Murcia/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Murcia/murcia-desconectar.jpg
%{_datadir}/gdm/themes/Murcia/murcia.jpg
%{_datadir}/gdm/themes/Murcia/murcia-opciones.jpg
%{_datadir}/gdm/themes/Murcia/murcia-sesion.jpg
%{_datadir}/gdm/themes/Murcia/murcia-sistema.jpg
%{_datadir}/gdm/themes/Murcia/murcia.xml
%{_datadir}/gdm/themes/Murcia/screenshot.jpg

#
# Theme 58/80
#
%files Open_Source_Initiative
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Open_Source_Initiative
%{_datadir}/gdm/themes/Open_Source_Initiative/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Open_Source_Initiative/language.png
%{_datadir}/gdm/themes/Open_Source_Initiative/open_source.png
%{_datadir}/gdm/themes/Open_Source_Initiative/open_source.xml
%{_datadir}/gdm/themes/Open_Source_Initiative/options.png
%{_datadir}/gdm/themes/Open_Source_Initiative/quit.png
%{_datadir}/gdm/themes/Open_Source_Initiative/screenshot.png
%{_datadir}/gdm/themes/Open_Source_Initiative/session.png
%{_datadir}/gdm/themes/Open_Source_Initiative/system.png

#
# Theme 59/80
#
%files Penguin_Computing
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Penguin_Computing
%{_datadir}/gdm/themes/Penguin_Computing/background.jpg
%{_datadir}/gdm/themes/Penguin_Computing/disconnect.png
%{_datadir}/gdm/themes/Penguin_Computing/galikynes.jpg
%{_datadir}/gdm/themes/Penguin_Computing/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Penguin_Computing/option.png
%{_datadir}/gdm/themes/Penguin_Computing/penguin.xml
%{_datadir}/gdm/themes/Penguin_Computing/session.png
%{_datadir}/gdm/themes/Penguin_Computing/system.png

#
# Theme 60/80
#
%files Peppe_for_Gonme
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Peppe_for_Gonme
%{_datadir}/gdm/themes/Peppe_for_Gonme/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Peppe_for_Gonme/lingua.png
%{_datadir}/gdm/themes/Peppe_for_Gonme/login.png
%{_datadir}/gdm/themes/Peppe_for_Gonme/logo.png
%{_datadir}/gdm/themes/Peppe_for_Gonme/screenshot.png
%{_datadir}/gdm/themes/Peppe_for_Gonme/servizi.png
%{_datadir}/gdm/themes/Peppe_for_Gonme/sessioni.png
%{_datadir}/gdm/themes/Peppe_for_Gonme/sfondo.svg
%{_datadir}/gdm/themes/Peppe_for_Gonme/theme.xml

#
# Theme 61/80
#
%files pixelGDM
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/pixelGDM
%{_datadir}/gdm/themes/pixelGDM/background.png
%{_datadir}/gdm/themes/pixelGDM/disconnect_over.png
%{_datadir}/gdm/themes/pixelGDM/disconnect.png
%{_datadir}/gdm/themes/pixelGDM/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/pixelGDM/language_over.png
%{_datadir}/gdm/themes/pixelGDM/language.png
%{_datadir}/gdm/themes/pixelGDM/pixelGDM.xml
%{_datadir}/gdm/themes/pixelGDM/screenshot.jpg
%{_datadir}/gdm/themes/pixelGDM/screenshot-small.png
%{_datadir}/gdm/themes/pixelGDM/session_over.png
%{_datadir}/gdm/themes/pixelGDM/session.png
%{_datadir}/gdm/themes/pixelGDM/shutdown_over.png
%{_datadir}/gdm/themes/pixelGDM/shutdown.png
%{_datadir}/gdm/themes/pixelGDM/system_over.png
%{_datadir}/gdm/themes/pixelGDM/system.png

#
# Theme 62/80
#
%files Red_Leaves
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Red_Leaves
%{_datadir}/gdm/themes/Red_Leaves/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Red_Leaves/leaves.png
%{_datadir}/gdm/themes/Red_Leaves/leaves-screenshot.png
%{_datadir}/gdm/themes/Red_Leaves/leaves.xml
%{_datadir}/gdm/themes/Red_Leaves/options.png

#
# Theme 63/80
#
%files RightVision
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/RightVision
%{_datadir}/gdm/themes/RightVision/background.jpg
%{_datadir}/gdm/themes/RightVision/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/RightVision/logorv.gif
%{_datadir}/gdm/themes/RightVision/oeil1.png
%{_datadir}/gdm/themes/RightVision/oeil2.png
%{_datadir}/gdm/themes/RightVision/oeil3.png
%{_datadir}/gdm/themes/RightVision/oeil4.png
%{_datadir}/gdm/themes/RightVision/rv.xml
%{_datadir}/gdm/themes/RightVision/screenshot.png

#
# Theme 64/80
#
%files Sea
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Sea
%{_datadir}/gdm/themes/Sea/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Sea/help.png
%{_datadir}/gdm/themes/Sea/options.png
%{_datadir}/gdm/themes/Sea/screenshot.jpg
%{_datadir}/gdm/themes/Sea/sea.jpg
%{_datadir}/gdm/themes/Sea/sea.xml

#
# Theme 65/80
#
%files Segovia
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Segovia
%{_datadir}/gdm/themes/Segovia/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Segovia/screenshot.jpg
%{_datadir}/gdm/themes/Segovia/segovia1.jpg
%{_datadir}/gdm/themes/Segovia/segovia2.jpg
%{_datadir}/gdm/themes/Segovia/segovia3.jpg
%{_datadir}/gdm/themes/Segovia/segovia4.jpg
%{_datadir}/gdm/themes/Segovia/segovia.jpg
%{_datadir}/gdm/themes/Segovia/segovia.xml

#
# Theme 66/80
#
%files Segovia_Night
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Segovia_Night
%{_datadir}/gdm/themes/Segovia_Night/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Segovia_Night/screenshot.jpg
%{_datadir}/gdm/themes/Segovia_Night/segovia1.jpg
%{_datadir}/gdm/themes/Segovia_Night/segovia2.jpg
%{_datadir}/gdm/themes/Segovia_Night/segovia3.jpg
%{_datadir}/gdm/themes/Segovia_Night/segovia4.jpg
%{_datadir}/gdm/themes/Segovia_Night/segovia-night.jpg
%{_datadir}/gdm/themes/Segovia_Night/segovia-night.xml

#
# Theme 67/80
#
%files Shapy
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Shapy
%{_datadir}/gdm/themes/Shapy/background.png
%{_datadir}/gdm/themes/Shapy/config.xml
%{_datadir}/gdm/themes/Shapy/disconnect.png
%{_datadir}/gdm/themes/Shapy/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Shapy/option.png
%{_datadir}/gdm/themes/Shapy/README
%{_datadir}/gdm/themes/Shapy/screenshot.png
%{_datadir}/gdm/themes/Shapy/session.png
%{_datadir}/gdm/themes/Shapy/system.png

#
# Theme 68/80
#
%files Simple-Gnome-Logo
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Simple-Gnome-Logo
%{_datadir}/gdm/themes/Simple-Gnome-Logo/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Simple-Gnome-Logo/gnome-foot-black.png
%{_datadir}/gdm/themes/Simple-Gnome-Logo/Gnome-Logo.xml
%{_datadir}/gdm/themes/Simple-Gnome-Logo/options.png

#
# Theme 69/80
#
%files Space
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Space
%{_datadir}/gdm/themes/Space/background.jpg
%{_datadir}/gdm/themes/Space/ball.png
%{_datadir}/gdm/themes/Space/disconnect.png
%{_datadir}/gdm/themes/Space/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Space/option.png
%{_datadir}/gdm/themes/Space/screenshot.jpg
%{_datadir}/gdm/themes/Space/session.png
%{_datadir}/gdm/themes/Space/space.xml
%{_datadir}/gdm/themes/Space/system.png

#
# Theme 71/80
#
%files SpreadFirefox
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/SpreadFirefox
%{_datadir}/gdm/themes/SpreadFirefox/firefox.jpg
%{_datadir}/gdm/themes/SpreadFirefox/firefox.xml
%{_datadir}/gdm/themes/SpreadFirefox/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/SpreadFirefox/options.png
%{_datadir}/gdm/themes/SpreadFirefox/screenshot.png

#
# Theme 72/80
#
%files STGO
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/STGO
%{_datadir}/gdm/themes/STGO/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/STGO/screenshot.jpg
%{_datadir}/gdm/themes/STGO/stgo1.jpg
%{_datadir}/gdm/themes/STGO/stgo2.jpg
%{_datadir}/gdm/themes/STGO/stgo3.jpg
%{_datadir}/gdm/themes/STGO/stgo4.jpg
%{_datadir}/gdm/themes/STGO/stgo.jpg
%{_datadir}/gdm/themes/STGO/stgo.xml

#
# Theme 73/80
#
%files Stop_TCPA
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Stop_TCPA
%{_datadir}/gdm/themes/Stop_TCPA/background.jpg
%{_datadir}/gdm/themes/Stop_TCPA/disconnect.png
%{_datadir}/gdm/themes/Stop_TCPA/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Stop_TCPA/option.png
%{_datadir}/gdm/themes/Stop_TCPA/session.png
%{_datadir}/gdm/themes/Stop_TCPA/system.png
%{_datadir}/gdm/themes/Stop_TCPA/tcpa.xml

#
# Theme 74/80
#
%files SVG_Sakura
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/SVG_Sakura
%{_datadir}/gdm/themes/SVG_Sakura/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/SVG_Sakura/gdm_shot.png
%{_datadir}/gdm/themes/SVG_Sakura/options_color.svg
%{_datadir}/gdm/themes/SVG_Sakura/options.png
%{_datadir}/gdm/themes/SVG_Sakura/options.svg
%{_datadir}/gdm/themes/SVG_Sakura/readme
%{_datadir}/gdm/themes/SVG_Sakura/sakura.svg
%{_datadir}/gdm/themes/SVG_Sakura/sakura.xml

#
# Theme 75/80
#
%files Synergy
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Synergy
%{_datadir}/gdm/themes/Synergy/background.png
%{_datadir}/gdm/themes/Synergy/disconnect.png
%{_datadir}/gdm/themes/Synergy/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Synergy/halt.png
%{_datadir}/gdm/themes/Synergy/options.png
%{_datadir}/gdm/themes/Synergy/reboot.png
%{_datadir}/gdm/themes/Synergy/screenshot.jpg
%{_datadir}/gdm/themes/Synergy/session.png
%{_datadir}/gdm/themes/Synergy/theme.xml

#
# Theme 76/80
#
%files Taipei
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Taipei
%{_datadir}/gdm/themes/Taipei/background.jpg
%{_datadir}/gdm/themes/Taipei/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Taipei/help.png
%{_datadir}/gdm/themes/Taipei/options.png
%{_datadir}/gdm/themes/Taipei/Taipei.jpg
%{_datadir}/gdm/themes/Taipei/theme.xml

#
# Theme 77/80
#
%files The_Dark_Crystal
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/The_Dark_Crystal
%{_datadir}/gdm/themes/The_Dark_Crystal/background.png
%{_datadir}/gdm/themes/The_Dark_Crystal/darkcrystal.xml
%{_datadir}/gdm/themes/The_Dark_Crystal/disconnect.png
%{_datadir}/gdm/themes/The_Dark_Crystal/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/The_Dark_Crystal/language.png
%{_datadir}/gdm/themes/The_Dark_Crystal/session.png
%{_datadir}/gdm/themes/The_Dark_Crystal/system.png

#
# Theme 78/80
#
%files Todmorden
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Todmorden
%{_datadir}/gdm/themes/Todmorden/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Todmorden/help.png
%{_datadir}/gdm/themes/Todmorden/options.png
%{_datadir}/gdm/themes/Todmorden/screenshot.jpg
%{_datadir}/gdm/themes/Todmorden/todmorden.jpg
%{_datadir}/gdm/themes/Todmorden/todmorden.xml

#
# Theme 79/80
#
%files Valladolid
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/Valladolid
%{_datadir}/gdm/themes/Valladolid/ava-desconectar.jpg
%{_datadir}/gdm/themes/Valladolid/ava-opcion.jpg
%{_datadir}/gdm/themes/Valladolid/ava-sesion.jpg
%{_datadir}/gdm/themes/Valladolid/ava-sistema.jpg
%{_datadir}/gdm/themes/Valladolid/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Valladolid/screenshot.jpg
%{_datadir}/gdm/themes/Valladolid/valladolid.jpg
%{_datadir}/gdm/themes/Valladolid/valladolid.xml

#
# Theme 80/80
#
%files XPTO
%defattr(644,root,root,755)
%dir %{_datadir}/gdm/themes/XPTO
%{_datadir}/gdm/themes/XPTO/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/XPTO/language.png
%{_datadir}/gdm/themes/XPTO/options.png
%{_datadir}/gdm/themes/XPTO/quit.png
%{_datadir}/gdm/themes/XPTO/session.png
%{_datadir}/gdm/themes/XPTO/system.png
%{_datadir}/gdm/themes/XPTO/xpto_bg.jpg
%{_datadir}/gdm/themes/XPTO/xpto.jpg
%{_datadir}/gdm/themes/XPTO/xpto_shot.png
%{_datadir}/gdm/themes/XPTO/xpto.xml
%{_datadir}/gdm/themes/XPTO/xpt.xml
