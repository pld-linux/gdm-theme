# TODO:
#   - fix bogus (non-informative, English-in-pl) descriptions
#   - add missing %dirs
#
Summary:	Themes for gdm (GNOME Display Manager)
Summary(pl):	Motywy dla gdm (Zarz±dcy ekranów GNOME)
Name:		gdm-theme
Version:	2.4.4.5
Release:	1
License:	GPL
Group:		Themes
URL:		http://art.gnome.org/
Requires:	gdm
BuildRequires:	tar
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#
# This spec is generated from ./gdm-themes-spec-generator.sh script.
# You should find it in your `rpm --eval %_specdir`
#
Source0:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Morning.tar.bz2
# Source0-md5:	b6ffafe1d608d4f345c3c6fac0cba29f
Source1:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-RedHat.tar.bz2
# Source1-md5:	e3dae3315631938b469b954c2eccaa31
Source2:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Sea.tar.gz
# Source2-md5:	0a200b93f8081df5d3c779281c6b2bfc
Source3:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Segovia-Night.tar.gz
# Source3-md5:	a85f01841618f29e9f01a307e77041dd
Source4:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-STGO.tar.gz
# Source4-md5:	7961582f7bfc80accc7c3a9a6c1c42a8
Source5:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-SUSE.tar.gz
# Source5-md5:	f647e392aa0251c67ae25baab30d5625
Source6:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Segovia.tar.gz
# Source6-md5:	ce5a826adad38d70bd42bb2a21a87074
Source7:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Bluecurve.tar.gz
# Source7-md5:	d5ecea20b85e033adcfa2d8d37f6abc8
Source8:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-300-lantueno.tar.gz
# Source8-md5:	9fc35fec651a220abc0eb664e84cedd4
Source9:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-xpto.tar.gz
# Source9-md5:	adcdc03f36d9a9c72d64a77ba98f5045
Source10:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Dawn.tar.gz
# Source10-md5:	5d81c298745480ca3d512a72429eb445
Source11:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-GlassFoot.tar.gz
# Source11-md5:	5220133ad1b367500b559d57cc1eb02f
Source12:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Space.tar.gz
# Source12-md5:	76e87a0979f225879422399ddb5673d8
Source13:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Flame.tar.gz
# Source13-md5:	82219dd6ec558efbf0fb81ce4b27eb4c
Source14:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Unxstar.tar.gz
# Source14-md5:	caca5b4b29631dd183d1bbbe03c64421
Source15:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Slackgdm.tar.gz
# Source15-md5:	8e75735be8f391931d9e9e6570708e2d
Source16:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Hybridfusion.tar.gz
# Source16-md5:	9397e525790f0232ec9f45d48649f07e
Source17:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Barna.tar.gz
# Source17-md5:	3260910713ceedcee3206ad4f4ca550c
Source18:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Valladolid.tar.gz
# Source18-md5:	1530c57898443bc3336cc4612a572055
Source19:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Murcia.tgz
# Source19-md5:	057d34a3435af7dbdc9637d2c2ec3dc7
Source20:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Leon.tar.gz
# Source20-md5:	ea73242c8f54aaf9650453cefbc9b897
Source21:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Gentoo-Emergence.tar.gz
# Source21-md5:	fec808ce063e212b7d48246f555819de
Source22:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-FreeBSD.tar.gz
# Source22-md5:	8bd68b2a87c09943b150ef671a4327a9
Source23:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Daybreak.tar.gz
# Source23-md5:	238e80b7b1e4105cce13f381689ce761
Source24:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Bijou.tgz
# Source24-md5:	20fafc60a0a7f163d03c602e912f3660
Source25:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Tcpa.tar.gz
# Source25-md5:	144240a042baff4af3e0fd1a2a509f1a
Source26:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-OpenSource.tgz
# Source26-md5:	1845e772f6b5ca0bcfdfacb5b68f9d1f
Source27:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-FreeBSDarth.tar.gz
# Source27-md5:	b59d9123f544a77f8b26b9198c5babef
Source28:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-penguin.tar.gz
# Source28-md5:	19de4049ad36693e9c9aafe373c2c7ca
Source29:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Knoke.tar.gz
# Source29-md5:	32378f58ab198dbe4bd2ad9709ac8bf6
Source30:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Darkcrystal.tar.bz2
# Source30-md5:	d6d8c3cab9c1790db3bcd05596f4cf75
Source31:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Chilie.tar.gz
# Source31-md5:	a115430ff4925efd65047de7e81e31c8
Source32:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Glassy.tar.gz
# Source32-md5:	b4db73c515b95cec7c72514b53d96413
Source33:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-MachuPicchu.tar.gz
# Source33-md5:	fd876d92468e4881ec8213e69e79ec9f
Source34:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-RV.tar.gz
# Source34-md5:	929027123d47db1a4e5f8cd41493739a
Source35:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-labisbal.tar.gz
# Source35-md5:	dd6b2d7d8fd40a82adab35707b828eab
Source36:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Falling-Angel.tar.gz
# Source36-md5:	95c2d2f79cb72a47d26b373e603ed250
Source37:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Hantzley.tar.gz
# Source37-md5:	3e1678c28a82e6ac814d0f250d71a727
Source38:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Mozi.tar.gz
# Source38-md5:	0ea48d8805189567a92fe987b959bacd
Source39:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Todmorden.tar.gz
# Source39-md5:	c6222e888f43c83243a61083d5afb324
Source40:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Hunter.tar.gz
# Source40-md5:	50abd5fbb23e22914a6654d4903a6833
Source41:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Mosaic.tar.gz
# Source41-md5:	a4673c14f17fb129f07348b4bd2a9382
Source42:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-KDE-Crystal.tar.gz
# Source42-md5:	3bd019cf594a6ef78a5dab0bc9b8023f
Source43:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Crystal-Rose.tar.gz
# Source43-md5:	4ab12cbdb57c77320b0cf9790ce4daae
Source44:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-DevilsCandy.tar.gz
# Source44-md5:	60c44dd459386f60bffa1698bedca9e2
Source45:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Synergy.tar.gz
# Source45-md5:	a0cb7549b2507eb9fac2995996f0bc53
Source46:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Cubic_Linux_Gnome.tar.gz
# Source46-md5:	95ed3fc14f07489a6bfad75db0b908f1
Source47:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Butterfly.tar.gz
# Source47-md5:	821f9da7a5a6f00a682fd46481a0ad59
Source48:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Mirrored-0.8.tar.gz
# Source48-md5:	97f308b23e5643fc14e9817168796879
Source49:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Delicious.tar.gz
# Source49-md5:	1af671d07921b39278dd27cff8ea4247
Source50:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-BlueSlack.tar.gz
# Source50-md5:	de1ab89b3b618e268ea2f221c2d10be9
Source51:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Dreaming-Alien.tar.gz
# Source51-md5:	a9d8e1dc49408e32571fc4985cfbb4f3
Source52:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-gcr-ddlm.tar.gz
# Source52-md5:	91ebc74754d87bf8f6def76bbe8e5844
Source53:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-gentoo-cow.tar.bz2
# Source53-md5:	e0dcf60fc342ed1862f0fff26da984b2
Source54:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-JustBSD.tar.gz
# Source54-md5:	7dbdb8b1561c23b1c58056716cb7843d
Source55:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-pixelgdm.tar.gz
# Source55-md5:	218d02a637ee040450fd6f08039011de
Source56:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Red-Leaves.tar.gz
# Source56-md5:	f2c0b9aa3638dbfef408a1d4a270eaaa
Source57:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-MonoMetal.tar.gz
# Source57-md5:	178fb25cfc57997e63cecc5279e7a0dd
Source58:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Dropline.tar.gz
# Source58-md5:	4ce8fd37e8bb56183ff78c40dcaad7f6
Source59:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-BeeAtWork.tar.gz
# Source59-md5:	809566fd4f2cdc3e8d282b8328a8b2be
Source60:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-LinuxTux.tar.gz
# Source60-md5:	2334031099d73c3afe2d4a05633a6634
Source61:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Taipei.tar.gz
# Source61-md5:	20c3d22c3622bf5f2fc1f3e771913145
Source62:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Odysseus.tar.gz
# Source62-md5:	c1ab56b4017f45614fccec3e9fbbde81
Source63:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Kinkakuji.tar.gz
# Source63-md5:	d35e28892c37a5c445bccb3c8f30de60
Source64:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Milk.tar.gz
# Source64-md5:	faf11a2f6e7ff36a822bd553b6cdbe21
Source65:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Cropcircles.tar.bz2
# Source65-md5:	7ea42e8a66188195d4b37d612c6b62d7
Source66:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Angel.tar.gz
# Source66-md5:	56c714da16420342d22659108055b647
Source67:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Blueish.tar.gz
# Source67-md5:	b56faca3944bdc59e941b44197e89677
Source68:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Cracked-Windows.tar.gz
# Source68-md5:	4103efc6f74f54a83b172616167cb108
Source69:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Crystal.tar.gz
# Source69-md5:	f89c4b0c29aec5d285ff2ce0199870a5
Source70:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-DartFrog.tar.bz2
# Source70-md5:	5ebb26d03f7eab3ac725ebb33c2becf6
Source71:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-DumbCloud.tar.gz
# Source71-md5:	8da61b45e88602adcad82c8b92869604
Source72:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Emo-Blue.tar.gz
# Source72-md5:	5dcbf93484203a9e594264878a8e7699
Source73:	http://ftp.gnome.org/pub/GNOME/teams/art.gnome.org/themes/gdm_greeter/GDM-Flowers.tar.gz
# Source73-md5:	7763649e7acca699bb25df0fc6e1c079

%description
This package allows you to change the look of your GNOME Display
Manager :-)

%description -l pl
Ten pakiet pozwala na zmiane wygl±du Zarz±dcy ekranów GNOME :-)

%package Morning_Light
Summary:	Theme Morning_Light for gdm (GNOME Display Manager)
Summary(pl):	Motyw Morning_Light dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Moses Lei
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/103.php
Requires:	%{name}

%description Morning_Light
Theme 'Morning_Light' by 'Moses Lei'. Author comment for the theme:
Background by Ryan Bliss, http://www.digitalblasphemy.com/ .

%description Morning_Light -l pl
Motyw 'Morning_Light' autorstwa 'Moses Lei'. Komentarz autora do
motywu: Background by Ryan Bliss, http://www.digitalblasphemy.com/ .

%package RedHat
Summary:	Theme RedHat for gdm (GNOME Display Manager)
Summary(pl):	Motyw RedHat dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Hakim Meskine
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/105.php
Requires:	%{name}

%description RedHat
Theme 'RedHat' by 'Hakim Meskine'. Author comment for the theme: I
borrowed the background. Thanks to shanuxnox at yahoo.com.

%description RedHat -l pl
Motyw 'RedHat' autorstwa 'Hakim Meskine'. Komentarz autora do motywu:
I borrowed the background. Thanks to shanuxnox at yahoo.com.

%package Sea
Summary:	Theme Sea for gdm (GNOME Display Manager)
Summary(pl):	Motyw Sea dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Gianluca Masci
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/107.php
Requires:	%{name}

%description Sea
Theme 'Sea' by 'Gianluca Masci'. Author comment for the theme: A "Sea
and Sunset" theme.

%description Sea -l pl
Motyw 'Sea' autorstwa 'Gianluca Masci'. Komentarz autora do motywu: A
"Sea and Sunset" theme.

%package Segovia_Night
Summary:	Theme Segovia_Night for gdm (GNOME Display Manager)
Summary(pl):	Motyw Segovia_Night dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Alvaro del Castillo
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/108.php
Requires:	%{name}

%description Segovia_Night
Theme 'Segovia_Night' by 'Alvaro del Castillo'. Author comment for the
theme: A Spanish historical city in the night.

%description Segovia_Night -l pl
Motyw 'Segovia_Night' autorstwa 'Alvaro del Castillo'. Komentarz
autora do motywu: A Spanish historical city in the night.

%package STGO
Summary:	Theme STGO for gdm (GNOME Display Manager)
Summary(pl):	Motyw STGO dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Phillip
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/109.php
Requires:	%{name}

%description STGO
Theme 'STGO' by 'Phillip'. Author comment for the theme: A photo from
Santiago.

%description STGO -l pl
Motyw 'STGO' autorstwa 'Phillip'. Komentarz autora do motywu: A photo
from Santiago.

%package SuSE
Summary:	Theme SuSE for gdm (GNOME Display Manager)
Summary(pl):	Motyw SuSE dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Johnathan Bailes
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/110.php
Requires:	%{name}

%description SuSE
Theme 'SuSE' by 'Johnathan Bailes'. Author comment for the theme: A
SuSE based version of the wonderful RedHat GDM theme.

%description SuSE -l pl
Motyw 'SuSE' autorstwa 'Johnathan Bailes'. Komentarz autora do motywu:
A SuSE based version of the wonderful RedHat GDM theme.

%package Segovia
Summary:	Theme Segovia for gdm (GNOME Display Manager)
Summary(pl):	Motyw Segovia dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Alvaro del Castillo
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/111.php
Requires:	%{name}

%description Segovia
Theme 'Segovia' by 'Alvaro del Castillo'. Author comment for the
theme: A Spanish historical city.

%description Segovia -l pl
Motyw 'Segovia' autorstwa 'Alvaro del Castillo'. Komentarz autora do
motywu: A Spanish historical city.

%package Bluecurve
Summary:	Theme Bluecurve for gdm (GNOME Display Manager)
Summary(pl):	Motyw Bluecurve dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Garrett LeSage
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/161.php
Requires:	%{name}

%description Bluecurve
Theme 'Bluecurve' by 'Garrett LeSage'. Author comment for the theme:
This theme is shipped with RedHat 8.0.

%description Bluecurve -l pl
Motyw 'Bluecurve' autorstwa 'Garrett LeSage'. Komentarz autora do
motywu: This theme is shipped with RedHat 8.0.

%package 300-lantueno
Summary:	Theme 300-lantueno for gdm (GNOME Display Manager)
Summary(pl):	Motyw 300-lantueno dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Naciu
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/178.php
Requires:	%{name}

%description 300-lantueno
Theme '300-lantueno' by 'Naciu'. Author comment for the theme: Theme
based on Lantueno ; year 1911 (Cantabria, Spain).

%description 300-lantueno -l pl
Motyw '300-lantueno' autorstwa 'Naciu'. Komentarz autora do motywu:
Theme based on Lantueno ; year 1911 (Cantabria, Spain).

%package XPTO
Summary:	Theme XPTO for gdm (GNOME Display Manager)
Summary(pl):	Motyw XPTO dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Nelson Marques
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/182.php
Requires:	%{name}

%description XPTO
Theme 'XPTO' by 'Nelson Marques'. Author comment for the theme: A
theme made for the common GDM login's of our humble machines.

%description XPTO -l pl
Motyw 'XPTO' autorstwa 'Nelson Marques'. Komentarz autora do motywu: A
theme made for the common GDM login's of our humble machines.

%package Dawn
Summary:	Theme Dawn for gdm (GNOME Display Manager)
Summary(pl):	Motyw Dawn dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Gianluca Masci
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/184.php
Requires:	%{name}

%description Dawn
Theme 'Dawn' by 'Gianluca Masci'. Author comment for the theme: Dawn
in mountain.

%description Dawn -l pl
Motyw 'Dawn' autorstwa 'Gianluca Masci'. Komentarz autora do motywu:
Dawn in mountain.

%package GDM-GlassFoot
Summary:	Theme GDM-GlassFoot for gdm (GNOME Display Manager)
Summary(pl):	Motyw GDM-GlassFoot dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Burcin Donmez
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/196.php
Requires:	%{name}

%description GDM-GlassFoot
Theme 'GDM-GlassFoot' by 'Burcin Donmez'. Author comment for the
theme: GDM greeter using GNOME-GlassFoot background image from
Waldgeist.

%description GDM-GlassFoot -l pl
Motyw 'GDM-GlassFoot' autorstwa 'Burcin Donmez'. Komentarz autora do
motywu: GDM greeter using GNOME-GlassFoot background image from
Waldgeist.

%package Space
Summary:	Theme Space for gdm (GNOME Display Manager)
Summary(pl):	Motyw Space dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Guille (bisho)
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/222.php
Requires:	%{name}

%description Space
Theme 'Space' by 'Guille (bisho)'. Author comment for the theme: A
space based greeter with icons borrowed from other themes.

%description Space -l pl
Motyw 'Space' autorstwa 'Guille (bisho)'. Komentarz autora do motywu:
A space based greeter with icons borrowed from other themes.

%package Fire_Breathing_Robot
Summary:	Theme Fire_Breathing_Robot for gdm (GNOME Display Manager)
Summary(pl):	Motyw Fire_Breathing_Robot dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		John Cantrell
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/223.php
Requires:	%{name}

%description Fire_Breathing_Robot
Theme 'Fire_Breathing_Robot' by 'John Cantrell'. Author comment for
the theme: A neat little fire breathing robot for your login. Based
off the Redhat's bluecurve.

%description Fire_Breathing_Robot -l pl
Motyw 'Fire_Breathing_Robot' autorstwa 'John Cantrell'. Komentarz
autora do motywu: A neat little fire breathing robot for your login.
Based off the Redhat's bluecurve.

%package UnxStar
Summary:	Theme UnxStar for gdm (GNOME Display Manager)
Summary(pl):	Motyw UnxStar dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Adriel Cardenas G.
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/232.php
Requires:	%{name}

%description UnxStar
Theme 'UnxStar' by 'Adriel Cardenas G.'. Author comment for the theme:
Cool FreeBSD Daemon with tux in the back and the java fella. All about
UNX.

%description UnxStar -l pl
Motyw 'UnxStar' autorstwa 'Adriel Cardenas G.'. Komentarz autora do
motywu: Cool FreeBSD Daemon with tux in the back and the java fella.
All about UNX.

%package SlackGDM
Summary:	Theme SlackGDM for gdm (GNOME Display Manager)
Summary(pl):	Motyw SlackGDM dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Marek A. Stepien
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/239.php
Requires:	%{name}

%description SlackGDM
Theme 'SlackGDM' by 'Marek A. Stepien'. Author comment for the theme:
This is a Slackware theme for GDM - for those of you who "got slack!"
:)

%description SlackGDM -l pl
Motyw 'SlackGDM' autorstwa 'Marek A. Stepien'. Komentarz autora do
motywu: This is a Slackware theme for GDM - for those of you who "got
slack!" :)

%package hybridFUSION
Summary:	Theme hybridFUSION for gdm (GNOME Display Manager)
Summary(pl):	Motyw hybridFUSION dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Vincent Mac
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/240.php
Requires:	%{name}

%description hybridFUSION
Theme 'hybridFUSION' by 'Vincent Mac'. Author comment for the theme:
hybridFUSION is a theme based on Night Elf with some different
artwork.

%description hybridFUSION -l pl
Motyw 'hybridFUSION' autorstwa 'Vincent Mac'. Komentarz autora do
motywu: hybridFUSION is a theme based on Night Elf with some different
artwork.

%package Barcelona
Summary:	Theme Barcelona for gdm (GNOME Display Manager)
Summary(pl):	Motyw Barcelona dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Álvaro del Castillo
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/241.php
Requires:	%{name}

%description Barcelona
Theme 'Barcelona' by 'Álvaro del Castillo'. Author comment for the
theme: Barcelona Spanish city.

%description Barcelona -l pl
Motyw 'Barcelona' autorstwa 'Álvaro del Castillo'. Komentarz autora do
motywu: Barcelona Spanish city.

%package Valladolid
Summary:	Theme Valladolid for gdm (GNOME Display Manager)
Summary(pl):	Motyw Valladolid dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Álvaro del Castillo
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/242.php
Requires:	%{name}

%description Valladolid
Theme 'Valladolid' by 'Álvaro del Castillo'. Author comment for the
theme: Valladolid spanish city

%description Valladolid -l pl
Motyw 'Valladolid' autorstwa 'Álvaro del Castillo'. Komentarz autora
do motywu: Valladolid spanish city

%package Murcia
Summary:	Theme Murcia for gdm (GNOME Display Manager)
Summary(pl):	Motyw Murcia dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Álvaro del Castillo
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/243.php
Requires:	%{name}

%description Murcia
Theme 'Murcia' by 'Álvaro del Castillo'. Author comment for the theme:
Murcia spanish city

%description Murcia -l pl
Motyw 'Murcia' autorstwa 'Álvaro del Castillo'. Komentarz autora do
motywu: Murcia spanish city

%package Leon
Summary:	Theme Leon for gdm (GNOME Display Manager)
Summary(pl):	Motyw Leon dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Álvaro del Castillo
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/244.php
Requires:	%{name}

%description Leon
Theme 'Leon' by 'Álvaro del Castillo'. Author comment for the theme:
Leon spanish city

%description Leon -l pl
Motyw 'Leon' autorstwa 'Álvaro del Castillo'. Komentarz autora do
motywu: Leon spanish city

%package Gentoo_Emergence
Summary:	Theme Gentoo_Emergence for gdm (GNOME Display Manager)
Summary(pl):	Motyw Gentoo_Emergence dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		okapi
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/245.php
Requires:	%{name}

%description Gentoo_Emergence
Theme 'Gentoo_Emergence' by 'okapi'. Author comment for the theme:
This is my first themes. Based on Emergence background created by Meir
Kriheli taken from Gentoo website
http://www.gentoo.org/main/en/graphics.xml. The framework was inspired
from the Angel theme from Bert De Meyer.

%description Gentoo_Emergence -l pl
Motyw 'Gentoo_Emergence' autorstwa 'okapi'. Komentarz autora do
motywu: This is my first themes. Based on Emergence background created
by Meir Kriheli taken from Gentoo website
http://www.gentoo.org/main/en/graphics.xml. The framework was inspired
from the Angel theme from Bert De Meyer.

%package FreeBSD_The_Power_of_Serve
Summary:	Theme FreeBSD_The_Power_of_Serve for gdm (GNOME Display Manager)
Summary(pl):	Motyw FreeBSD_The_Power_of_Serve dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Adriel Cardenas G.
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/255.php
Requires:	%{name}

%description FreeBSD_The_Power_of_Serve
Theme 'FreeBSD_The_Power_of_Serve' by 'Adriel Cardenas G.'. Author
comment for the theme: Cool FreeBSD Daemon on the back, and the
FreeBSD Systems logo and banner: The Power of Serve. :)

%description FreeBSD_The_Power_of_Serve -l pl
Motyw 'FreeBSD_The_Power_of_Serve' autorstwa 'Adriel Cardenas G.'
Komentarz autora do motywu: Cool FreeBSD Daemon on the back, and the
FreeBSD Systems logo and banner: The Power of Serve. :)

%package Daybreak
Summary:	Theme Daybreak for gdm (GNOME Display Manager)
Summary(pl):	Motyw Daybreak dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Francis Tyers
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/256.php
Requires:	%{name}

%description Daybreak
Theme 'Daybreak' by 'Francis Tyers'. Author comment for the theme:
Found a cool background on deviantart.com and set myself up the gdm
theme.

%description Daybreak -l pl
Motyw 'Daybreak' autorstwa 'Francis Tyers'. Komentarz autora do
motywu: Found a cool background on deviantart.com and set myself up
the gdm theme.

%package Bijou
Summary:	Theme Bijou for gdm (GNOME Display Manager)
Summary(pl):	Motyw Bijou dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Alex Fraser
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/257.php
Requires:	%{name}

%description Bijou
Theme 'Bijou' by 'Alex Fraser'. Author comment for the theme: Simple
and clean with highly polished buttons

%description Bijou -l pl
Motyw 'Bijou' autorstwa 'Alex Fraser'. Komentarz autora do motywu:
Simple and clean with highly polished buttons

%package Stop_TCPA
Summary:	Theme Stop_TCPA for gdm (GNOME Display Manager)
Summary(pl):	Motyw Stop_TCPA dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Lars Strojny
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/267.php
Requires:	%{name}

%description Stop_TCPA
Theme 'Stop_TCPA' by 'Lars Strojny'. Author comment for the theme: A
Theme against TCPA, Palladium and Censorship.

%description Stop_TCPA -l pl
Motyw 'Stop_TCPA' autorstwa 'Lars Strojny'. Komentarz autora do
motywu: A Theme against TCPA, Palladium and Censorship.

%package Open_Source_Initiative
Summary:	Theme Open_Source_Initiative for gdm (GNOME Display Manager)
Summary(pl):	Motyw Open_Source_Initiative dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Bryan W Clark
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/270.php
Requires:	%{name}

%description Open_Source_Initiative
Theme 'Open_Source_Initiative' by 'Bryan W Clark'. Author comment for
the theme: The Open Source Initiative (tm) logo http://opensource.org/
upgraded with a little gimp action.

%description Open_Source_Initiative -l pl
Motyw 'Open_Source_Initiative' autorstwa 'Bryan W Clark'. Komentarz
autora do motywu: The Open Source Initiative (tm) logo
http://opensource.org/ upgraded with a little gimp action.

%package FreeBSDarth
Summary:	Theme FreeBSDarth for gdm (GNOME Display Manager)
Summary(pl):	Motyw FreeBSDarth dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Adriel Cardenas G.
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/271.php
Requires:	%{name}

%description FreeBSDarth
Theme 'FreeBSDarth' by 'Adriel Cardenas G.'. Author comment for the
theme: FreeBSD Daemon with Darth Maul custom, over black background,
telling you the truth! : )

%description FreeBSDarth -l pl
Motyw 'FreeBSDarth' autorstwa 'Adriel Cardenas G.'. Komentarz autora
do motywu: FreeBSD Daemon with Darth Maul custom, over black
background, telling you the truth! : )

%package Penguin_Computing
Summary:	Theme Penguin_Computing for gdm (GNOME Display Manager)
Summary(pl):	Motyw Penguin_Computing dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Lars Strojny
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/272.php
Requires:	%{name}

%description Penguin_Computing
Theme 'Penguin_Computing' by 'Lars Strojny'. Author comment for the
theme: Theme which funny Quake-porting-image

%description Penguin_Computing -l pl
Motyw 'Penguin_Computing' autorstwa 'Lars Strojny'. Komentarz autora
do motywu: Theme which funny Quake-porting-image

%package Knoke
Summary:	Theme Knoke for gdm (GNOME Display Manager)
Summary(pl):	Motyw Knoke dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Dietrich Heise
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/278.php
Requires:	%{name}

%description Knoke
Theme 'Knoke' by 'Dietrich Heise'. Author comment for the theme: A GDM
Greeter Theme with my cat 'Knoke'.

%description Knoke -l pl
Motyw 'Knoke' autorstwa 'Dietrich Heise'. Komentarz autora do motywu:
A GDM Greeter Theme with my cat 'Knoke'.

%package The_Dark_Crystal
Summary:	Theme The_Dark_Crystal for gdm (GNOME Display Manager)
Summary(pl):	Motyw The_Dark_Crystal dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Bobby Corbell
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/293.php
Requires:	%{name}

%description The_Dark_Crystal
Theme 'The_Dark_Crystal' by 'Bobby Corbell'. Author comment for the
theme: A collage of images from the movie The Dark Crystal.

%description The_Dark_Crystal -l pl
Motyw 'The_Dark_Crystal' autorstwa 'Bobby Corbell'. Komentarz autora
do motywu: A collage of images from the movie The Dark Crystal.

%package Gnome_Chile
Summary:	Theme Gnome_Chile for gdm (GNOME Display Manager)
Summary(pl):	Motyw Gnome_Chile dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Andrés "Death_Knight" Villagrán
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/294.php
Requires:	%{name}

%description Gnome_Chile
Theme 'Gnome_Chile' by 'Andrés "Death_Knight" Villagrán'. Author
comment for the theme: EN: It's a best Theme of GNOME in Chile ES:
Este tema es exelente, bonito y muy atrallente MADE IN CHILE

%description Gnome_Chile -l pl
Motyw 'Gnome_Chile' autorstwa 'Andrés "Death_Knight" Villagrán'
Komentarz autora do motywu: EN: It's a best Theme of GNOME in Chile
ES: Este tema es exelente, bonito y muy atrallente MADE IN CHILE

%package Glassy
Summary:	Theme Glassy for gdm (GNOME Display Manager)
Summary(pl):	Motyw Glassy dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Christopher A. Shamis
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/298.php
Requires:	%{name}

%description Glassy
Theme 'Glassy' by 'Christopher A. Shamis'. Author comment for the
theme: Ray-traced glass cork-screw over a shiny checkered floor.

%description Glassy -l pl
Motyw 'Glassy' autorstwa 'Christopher A. Shamis'. Komentarz autora do
motywu: Ray-traced glass cork-screw over a shiny checkered floor.

%package Machu_Picchu
Summary:	Theme Machu_Picchu for gdm (GNOME Display Manager)
Summary(pl):	Motyw Machu_Picchu dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		David Thompson
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/300.php
Requires:	%{name}

%description Machu_Picchu
Theme 'Machu_Picchu' by 'David Thompson'. Author comment for the
theme: Pictures of the Inca remains at Machu Picchu in Peru.

%description Machu_Picchu -l pl
Motyw 'Machu_Picchu' autorstwa 'David Thompson'. Komentarz autora do
motywu: Pictures of the Inca remains at Machu Picchu in Peru.

%package RightVision
Summary:	Theme RightVision for gdm (GNOME Display Manager)
Summary(pl):	Motyw RightVision dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Thibaut Dabonneville & Alexandre Notteau
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/301.php
Requires:	%{name}

%description RightVision
Theme 'RightVision' by 'Thibaut Dabonneville & Alexandre Notteau'
Author comment for the theme: A colorfull theme used by linux users @
RightVision.

%description RightVision -l pl
Motyw 'RightVision' autorstwa 'Thibaut Dabonneville & Alexandre
Notteau'. Komentarz autora do motywu: A colorfull theme used by linux
users @ RightVision.

%package La_Bisbal_dEmpord_nevada
Summary:	Theme La_Bisbal_dEmpord_nevada for gdm (GNOME Display Manager)
Summary(pl):	Motyw La_Bisbal_dEmpord_nevada dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Radio Bisbal
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/303.php
Requires:	%{name}

%description La_Bisbal_dEmpord_nevada
Theme 'La_Bisbal_dEmpord_nevada' by 'Radio Bisbal'. Author comment for
the theme: Nice pictures taken after snowing at La Bisbal d'Empordà
(Catalonian town).

%description La_Bisbal_dEmpord_nevada -l pl
Motyw 'La_Bisbal_dEmpord_nevada' autorstwa 'Radio Bisbal'. Komentarz
autora do motywu: Nice pictures taken after snowing at La Bisbal
d'Empordà (Catalonian town).

%package Falling_Angel
Summary:	Theme Falling_Angel for gdm (GNOME Display Manager)
Summary(pl):	Motyw Falling_Angel dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Carlos (StackGuard) Ferreira
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/310.php
Requires:	%{name}

%description Falling_Angel
Theme 'Falling_Angel' by 'Carlos (StackGuard) Ferreira'. Author
comment for the theme: An atempt to make a GDM Greeter theme, based on
a beautyfull wallpaper :)

%description Falling_Angel -l pl
Motyw 'Falling_Angel' autorstwa 'Carlos (StackGuard) Ferreira'
Komentarz autora do motywu: An atempt to make a GDM Greeter theme,
based on a beautyfull wallpaper :)

%package Hantzley
Summary:	Theme Hantzley for gdm (GNOME Display Manager)
Summary(pl):	Motyw Hantzley dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Hantzley
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/311.php
Requires:	%{name}

%description Hantzley
Theme 'Hantzley' by 'Hantzley'. Author comment for the theme: My first
GDM Greeter Theme. Hope you like it

%description Hantzley -l pl
Motyw 'Hantzley' autorstwa 'Hantzley'. Komentarz autora do motywu: My
first GDM Greeter Theme. Hope you like it

%package Mozi
Summary:	Theme Mozi for gdm (GNOME Display Manager)
Summary(pl):	Motyw Mozi dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Soho501
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/325.php
Requires:	%{name}

%description Mozi
Theme 'Mozi' by 'Soho501'. Author comment for the theme: Iguana eating
msn butterfly

%description Mozi -l pl
Motyw 'Mozi' autorstwa 'Soho501'. Komentarz autora do motywu: Iguana
eating msn butterfly

%package Todmorden
Summary:	Theme Todmorden for gdm (GNOME Display Manager)
Summary(pl):	Motyw Todmorden dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Todd Jones
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/332.php
Requires:	%{name}

%description Todmorden
Theme 'Todmorden' by 'Todd Jones'. Author comment for the theme: A pic
I took from a hill over Todmorden, England.

%description Todmorden -l pl
Motyw 'Todmorden' autorstwa 'Todd Jones'. Komentarz autora do motywu:
A pic I took from a hill over Todmorden, England.

%package Hunter
Summary:	Theme Hunter for gdm (GNOME Display Manager)
Summary(pl):	Motyw Hunter dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Michael Thomas
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/33.php
Requires:	%{name}

%description Hunter
Theme 'Hunter' by 'Michael Thomas'. Author comment for the theme:
Circles theme that uses a image instead of a svg file.

%description Hunter -l pl
Motyw 'Hunter' autorstwa 'Michael Thomas'. Komentarz autora do motywu:
Circles theme that uses a image instead of a svg file.

%package GDM-Mosaic
Summary:	Theme GDM-Mosaic for gdm (GNOME Display Manager)
Summary(pl):	Motyw GDM-Mosaic dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		soho501
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/361.php
Requires:	%{name}

%description GDM-Mosaic
Theme 'GDM-Mosaic' by 'soho501'. Author comment for the theme: That's
the bull's shadow mosaic...

%description GDM-Mosaic -l pl
Motyw 'GDM-Mosaic' autorstwa 'soho501'. Komentarz autora do motywu:
That's the bull's shadow mosaic...

%package KDE_Crystal
Summary:	Theme KDE_Crystal for gdm (GNOME Display Manager)
Summary(pl):	Motyw KDE_Crystal dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Yann Bouan
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/396.php
Requires:	%{name}

%description KDE_Crystal
Theme 'KDE_Crystal' by 'Yann Bouan'. Author comment for the theme: A
theme inspired by the KDE crystal icon theme.

%description KDE_Crystal -l pl
Motyw 'KDE_Crystal' autorstwa 'Yann Bouan'. Komentarz autora do
motywu: A theme inspired by the KDE crystal icon theme.

%package Crystal_Rose
Summary:	Theme Crystal_Rose for gdm (GNOME Display Manager)
Summary(pl):	Motyw Crystal_Rose dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Carlos (StackGuard) Ferreira
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/403.php
Requires:	%{name}

%description Crystal_Rose
Theme 'Crystal_Rose' by 'Carlos (StackGuard) Ferreira'. Author comment
for the theme: Blue and shadded theme I've made for my girfriend,
based on a wallpaper found in deviantart.com

%description Crystal_Rose -l pl
Motyw 'Crystal_Rose' autorstwa 'Carlos (StackGuard) Ferreira'
Komentarz autora do motywu: Blue and shadded theme I've made for my
girfriend, based on a wallpaper found in deviantart.com

%package Devils_Candy
Summary:	Theme Devils_Candy for gdm (GNOME Display Manager)
Summary(pl):	Motyw Devils_Candy dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Slayer[nFc]
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/404.php
Requires:	%{name}

%description Devils_Candy
Theme 'Devils_Candy' by 'Slayer[nFc]'. Author comment for the theme:
My First GDM theme based on DevilsCandy by Xebra 2001

%description Devils_Candy -l pl
Motyw 'Devils_Candy' autorstwa 'Slayer[nFc]'. Komentarz autora do
motywu: My First GDM theme based on DevilsCandy by Xebra 2001

%package Synergy
Summary:	Theme Synergy for gdm (GNOME Display Manager)
Summary(pl):	Motyw Synergy dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		jam
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/419.php
Requires:	%{name}

%description Synergy
Theme 'Synergy' by 'jam'. Author comment for the theme: Synergy: cube
showing 2 faces. KDE logo on left face, GNOME logo on the other

%description Synergy -l pl
Motyw 'Synergy' autorstwa 'jam'. Komentarz autora do motywu: Synergy:
cube showing 2 faces. KDE logo on left face, GNOME logo on the other

%package Cubic_Linux_and_Gnome
Summary:	Theme Cubic_Linux_and_Gnome for gdm (GNOME Display Manager)
Summary(pl):	Motyw Cubic_Linux_and_Gnome dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		jam
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/420.php
Requires:	%{name}

%description Cubic_Linux_and_Gnome
Theme 'Cubic_Linux_and_Gnome' by 'jam'. Author comment for the theme:
Background is render of a cube showing 2 faces. Tux on 1 face, GNOME
logo on the other

%description Cubic_Linux_and_Gnome -l pl
Motyw 'Cubic_Linux_and_Gnome' autorstwa 'jam'. Komentarz autora do
motywu: Background is render of a cube showing 2 faces. Tux on 1 face,
GNOME logo on the other

%package Butterfly
Summary:	Theme Butterfly for gdm (GNOME Display Manager)
Summary(pl):	Motyw Butterfly dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		sgaap
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/443.php
Requires:	%{name}

%description Butterfly
Theme 'Butterfly' by 'sgaap'. Author comment for the theme: A bright
theme :)

%description Butterfly -l pl
Motyw 'Butterfly' autorstwa 'sgaap'. Komentarz autora do motywu: A
bright theme :)

%package Mirrored
Summary:	Theme Mirrored for gdm (GNOME Display Manager)
Summary(pl):	Motyw Mirrored dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Roman Joost
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/448.php
Requires:	%{name}

%description Mirrored
Theme 'Mirrored' by 'Roman Joost'. Author comment for the theme:
Mirrored desktop is a mirrored login screen with comic art. Not all of
the text is mirrored (for usability reasons).

%description Mirrored -l pl
Motyw 'Mirrored' autorstwa 'Roman Joost'. Komentarz autora do motywu:
Mirrored desktop is a mirrored login screen with comic art. Not all of
the text is mirrored (for usability reasons).

%package Delicious
Summary:	Theme Delicious for gdm (GNOME Display Manager)
Summary(pl):	Motyw Delicious dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Roman Joost
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/449.php
Requires:	%{name}

%description Delicious
Theme 'Delicious' by 'Roman Joost'. Author comment for the theme:
Delicious is a comic theme that uses clean icons and a funny
background.

%description Delicious -l pl
Motyw 'Delicious' autorstwa 'Roman Joost'. Komentarz autora do motywu:
Delicious is a comic theme that uses clean icons and a funny
background.

%package Blue_Slack_GDM
Summary:	Theme Blue_Slack_GDM for gdm (GNOME Display Manager)
Summary(pl):	Motyw Blue_Slack_GDM dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		elmaya
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/458.php
Requires:	%{name}

%description Blue_Slack_GDM
Theme 'Blue_Slack_GDM' by 'elmaya'. Author comment for the theme: A
simple blue GDM theme for Slackware.

%description Blue_Slack_GDM -l pl
Motyw 'Blue_Slack_GDM' autorstwa 'elmaya'. Komentarz autora do motywu:
A simple blue GDM theme for Slackware.

%package Dreaming_Alien
Summary:	Theme Dreaming_Alien for gdm (GNOME Display Manager)
Summary(pl):	Motyw Dreaming_Alien dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Christopher V. Browne
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/459.php
Requires:	%{name}

%description Dreaming_Alien
Theme 'Dreaming_Alien' by 'Christopher V. Browne'. Author comment for
the theme: Renoiro's Dreaming Alien - artist approved Buttons borrow
from Bijou.

%description Dreaming_Alien -l pl
Motyw 'Dreaming_Alien' autorstwa 'Christopher V. Browne'. Komentarz
autora do motywu: Renoiro's Dreaming Alien - artist approved Buttons
borrow from Bijou.

%package gcr-ddlm
Summary:	Theme gcr-ddlm for gdm (GNOME Display Manager)
Summary(pl):	Motyw gcr-ddlm dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		ghost_crab
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/460.php
Requires:	%{name}

%description gcr-ddlm
Theme 'gcr-ddlm' by 'ghost_crab'. Author comment for the theme: dia de
los muertos GDM theme. My first. Please let me know what I need to do
to fix it. Rock!

%description gcr-ddlm -l pl
Motyw 'gcr-ddlm' autorstwa 'ghost_crab'. Komentarz autora do motywu:
dia de los muertos GDM theme. My first. Please let me know what I need
to do to fix it. Rock!

%package Gentoo_Cow
Summary:	Theme Gentoo_Cow for gdm (GNOME Display Manager)
Summary(pl):	Motyw Gentoo_Cow dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Dennis
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/461.php
Requires:	%{name}

%description Gentoo_Cow
Theme 'Gentoo_Cow' by 'Dennis'. Author comment for the theme: This is
a modification of Redhat's Bluecurve gdm theme. I used a pixmap of the
gentoo cow (from the gentoo-artwork ebuild), and modified the colors
slightly.

%description Gentoo_Cow -l pl
Motyw 'Gentoo_Cow' autorstwa 'Dennis'. Komentarz autora do motywu:
This is a modification of Redhat's Bluecurve gdm theme. I used a
pixmap of the gentoo cow (from the gentoo-artwork ebuild), and
modified the colors slightly.

%package Just_BSD
Summary:	Theme Just_BSD for gdm (GNOME Display Manager)
Summary(pl):	Motyw Just_BSD dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Adriel Cardenas Guzman
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/462.php
Requires:	%{name}

%description Just_BSD
Theme 'Just_BSD' by 'Adriel Cardenas Guzman'. Author comment for the
theme: Virtual BSD Daemon.

%description Just_BSD -l pl
Motyw 'Just_BSD' autorstwa 'Adriel Cardenas Guzman'. Komentarz autora
do motywu: Virtual BSD Daemon.

%package pixelGDM
Summary:	Theme pixelGDM for gdm (GNOME Display Manager)
Summary(pl):	Motyw pixelGDM dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Roman Joost
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/463.php
Requires:	%{name}

%description pixelGDM
Theme 'pixelGDM' by 'Roman Joost'. Author comment for the theme:
pixelGDM is a theme with pixel icons.

%description pixelGDM -l pl
Motyw 'pixelGDM' autorstwa 'Roman Joost'. Komentarz autora do motywu:
pixelGDM is a theme with pixel icons.

%package Red_Leaves
Summary:	Theme Red_Leaves for gdm (GNOME Display Manager)
Summary(pl):	Motyw Red_Leaves dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Christopher "3-D" Fowler
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/464.php
Requires:	%{name}

%description Red_Leaves
Theme 'Red_Leaves' by 'Christopher "3-D" Fowler'. Author comment for
the theme: Japanese maple Red on a crisp blue fall sky makes a great
greeter.

%description Red_Leaves -l pl
Motyw 'Red_Leaves' autorstwa 'Christopher "3-D" Fowler'. Komentarz
autora do motywu: Japanese maple Red on a crisp blue fall sky makes a
great greeter.

%package Mono_Metal
Summary:	Theme Mono_Metal for gdm (GNOME Display Manager)
Summary(pl):	Motyw Mono_Metal dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		crahs
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/494.php
Requires:	%{name}

%description Mono_Metal
Theme 'Mono_Metal' by 'crahs'. Author comment for the theme: This is
my first theme, for GDM based on mono with metal style.

%description Mono_Metal -l pl
Motyw 'Mono_Metal' autorstwa 'crahs'. Komentarz autora do motywu: This
is my first theme, for GDM based on mono with metal style.

%package Gdm_Dropline
Summary:	Theme Gdm_Dropline for gdm (GNOME Display Manager)
Summary(pl):	Motyw Gdm_Dropline dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		elmaya
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/508.php
Requires:	%{name}

%description Gdm_Dropline
Theme 'Gdm_Dropline' by 'elmaya'. Author comment for the theme: A GDM
theme to go with the dropline splash screen

%description Gdm_Dropline -l pl
Motyw 'Gdm_Dropline' autorstwa 'elmaya'. Komentarz autora do motywu: A
GDM theme to go with the dropline splash screen

%package Bee_at_Work
Summary:	Theme Bee_at_Work for gdm (GNOME Display Manager)
Summary(pl):	Motyw Bee_at_Work dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Julian Coccia
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/509.php
Requires:	%{name}

%description Bee_at_Work
Theme 'Bee_at_Work' by 'Julian Coccia'. Author comment for the theme:
A nice GDM greeter theme in black and yellow, based on one of my
pictures.

%description Bee_at_Work -l pl
Motyw 'Bee_at_Work' autorstwa 'Julian Coccia'. Komentarz autora do
motywu: A nice GDM greeter theme in black and yellow, based on one of
my pictures.

%package LinuxTux
Summary:	Theme LinuxTux for gdm (GNOME Display Manager)
Summary(pl):	Motyw LinuxTux dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Rebel
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/511.php
Requires:	%{name}

%description LinuxTux
Theme 'LinuxTux' by 'Rebel'. Author comment for the theme: Tux
gdmgreeter

%description LinuxTux -l pl
Motyw 'LinuxTux' autorstwa 'Rebel'. Komentarz autora do motywu: Tux
gdmgreeter

%package Taipei
Summary:	Theme Taipei for gdm (GNOME Display Manager)
Summary(pl):	Motyw Taipei dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Julian Coccia
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/525.php
Requires:	%{name}

%description Taipei
Theme 'Taipei' by 'Julian Coccia'. Author comment for the theme:
Taipei, CKS Memorial Entrance (1600x1200)

%description Taipei -l pl
Motyw 'Taipei' autorstwa 'Julian Coccia'. Komentarz autora do motywu:
Taipei, CKS Memorial Entrance (1600x1200)

%package Odysseus
Summary:	Theme Odysseus for gdm (GNOME Display Manager)
Summary(pl):	Motyw Odysseus dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Markus Schatzl
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/526.php
Requires:	%{name}

%description Odysseus
Theme 'Odysseus' by 'Markus Schatzl'. Author comment for the theme:
Nothing done by myself except putting everything together.

%description Odysseus -l pl
Motyw 'Odysseus' autorstwa 'Markus Schatzl'. Komentarz autora do
motywu: Nothing done by myself except putting everything together.

%package Kinkakuji
Summary:	Theme Kinkakuji for gdm (GNOME Display Manager)
Summary(pl):	Motyw Kinkakuji dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Cholwich Nattee
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/527.php
Requires:	%{name}

%description Kinkakuji
Theme 'Kinkakuji' by 'Cholwich Nattee'. Author comment for the theme:
Kinkakuji (The temple of the Golden Pavilion) in Kyoto Japan.

%description Kinkakuji -l pl
Motyw 'Kinkakuji' autorstwa 'Cholwich Nattee'. Komentarz autora do
motywu: Kinkakuji (The temple of the Golden Pavilion) in Kyoto Japan.

%package Milk
Summary:	Theme Milk for gdm (GNOME Display Manager)
Summary(pl):	Motyw Milk dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Will Reinhart
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/533.php
Requires:	%{name}

%description Milk
Theme 'Milk' by 'Will Reinhart'. Author comment for the theme: A
graphical greeter theme with face browser. It is based on the
MilkGnome background by [Kony], Bluecurve icons, and the Happy GNOME
GDM theme. Requires GDM 2.4.2.95 or newer.

%description Milk -l pl
Motyw 'Milk' autorstwa 'Will Reinhart'. Komentarz autora do motywu: A
graphical greeter theme with face browser. It is based on the
MilkGnome background by [Kony], Bluecurve icons, and the Happy GNOME
GDM theme. Requires GDM 2.4.2.95 or newer.

%package Crop_Circles
Summary:	Theme Crop_Circles for gdm (GNOME Display Manager)
Summary(pl):	Motyw Crop_Circles dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Will Reinhart
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/543.php
Requires:	%{name}

%description Crop_Circles
Theme 'Crop_Circles' by 'Will Reinhart'. Author comment for the theme:
Signs of intelligent life! This is graphical face-browser theme, so it
requires GDM from GNOME 2.4.0. Thanks to Jiin Yaroon for the wallpaper
this theme's background is based on.

%description Crop_Circles -l pl
Motyw 'Crop_Circles' autorstwa 'Will Reinhart'. Komentarz autora do
motywu: Signs of intelligent life! This is graphical face-browser
theme, so it requires GDM from GNOME 2.4.0. Thanks to Jiin Yaroon for
the wallpaper this theme's background is based on.

%package Angel
Summary:	Theme Angel for gdm (GNOME Display Manager)
Summary(pl):	Motyw Angel dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Bert De Meyer
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/89.php
Requires:	%{name}

%description Angel
Theme 'Angel' by 'Bert De Meyer'. Author comment for the theme: Note:
This themes is based on an old Windowmaker theme from Largo that you
can still find at: <a
href=http://largo.windowmaker.org/themes/>http://largo.windowmaker.org/themes/

%description Angel -l pl
Motyw 'Angel' autorstwa 'Bert De Meyer'. Komentarz autora do motywu:
Note: This themes is based on an old Windowmaker theme from Largo that
you can still find at: <a
href=http://largo.windowmaker.org/themes/>http://largo.windowmaker.org/themes/

%package Blueish
Summary:	Theme Blueish for gdm (GNOME Display Manager)
Summary(pl):	Motyw Blueish dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Michael Thomas, Henrik Brix Andersen
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/90.php
Requires:	%{name}

%description Blueish
Theme 'Blueish' by 'Michael Thomas, Henrik Brix Andersen'. Author
comment for the theme: A metallic GNOME foot on a blue background.
Credits for the background goes to Henrik Brix Andersen.

%description Blueish -l pl
Motyw 'Blueish' autorstwa 'Michael Thomas, Henrik Brix Andersen'
Komentarz autora do motywu: A metallic GNOME foot on a blue
background. Credits for the background goes to Henrik Brix Andersen.

%package Cracked_Windows
Summary:	Theme Cracked_Windows for gdm (GNOME Display Manager)
Summary(pl):	Motyw Cracked_Windows dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Ovidiu Cernautan
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/91.php
Requires:	%{name}

%description Cracked_Windows
Theme 'Cracked_Windows' by 'Ovidiu Cernautan'. Author comment for the
theme: It's pretty colorful but I like it and I hope you'll like it
too.

%description Cracked_Windows -l pl
Motyw 'Cracked_Windows' autorstwa 'Ovidiu Cernautan'. Komentarz autora
do motywu: It's pretty colorful but I like it and I hope you'll like
it too.

%package Crystal
Summary:	Theme Crystal for gdm (GNOME Display Manager)
Summary(pl):	Motyw Crystal dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Niek van der Maas
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/92.php
Requires:	%{name}

%description Crystal
Theme 'Crystal' by 'Niek van der Maas'. Author comment for the theme:
Crystal Theme for GDM by Niek van der Maas. All images were made by
Everaldo.

%description Crystal -l pl
Motyw 'Crystal' autorstwa 'Niek van der Maas'. Komentarz autora do
motywu: Crystal Theme for GDM by Niek van der Maas. All images were
made by Everaldo.

%package Dart_Frog
Summary:	Theme Dart_Frog for gdm (GNOME Display Manager)
Summary(pl):	Motyw Dart_Frog dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Wreckd
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/93.php
Requires:	%{name}

%description Dart_Frog
Theme 'Dart_Frog' by 'Wreckd'. Author comment for the theme: Nice
little theme with a background I found. So, can anyone tell me what
kinda frog this is?

%description Dart_Frog -l pl
Motyw 'Dart_Frog' autorstwa 'Wreckd'. Komentarz autora do motywu: Nice
little theme with a background I found. So, can anyone tell me what
kinda frog this is?

%package DumbCloud
Summary:	Theme DumbCloud for gdm (GNOME Display Manager)
Summary(pl):	Motyw DumbCloud dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Unknown
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/96.php
Requires:	%{name}

%description DumbCloud
Theme 'DumbCloud' by 'Unknown'. Author comment for the theme: Dunno if
this is 'legal', I'm not an artist or technically inclined but I took
the photo of the cloud & made the image of lines & borrowed the other
graphics from the default Circles GDM greeter theme. I'm don't know
XML & don't want to learn it, so I only changed the filenames to
display my own. This is my attempt, its worse than the default one but
I just wanted to try it & have something different. For real artists,
just edit the files in /usr/share/gdm/themes - if I could do it, you
can.

%description DumbCloud -l pl
Motyw 'DumbCloud' autorstwa 'Unknown'. Komentarz autora do motywu:
Dunno if this is 'legal', I'm not an artist or technically inclined
but I took the photo of the cloud & made the image of lines & borrowed
the other graphics from the default Circles GDM greeter theme. I'm
don't know XML & don't want to learn it, so I only changed the
filenames to display my own. This is my attempt, its worse than the
default one but I just wanted to try it & have something different.
For real artists, just edit the files in /usr/share/gdm/themes - if I
could do it, you can.

%package Emo-Blue
Summary:	Theme Emo-Blue for gdm (GNOME Display Manager)
Summary(pl):	Motyw Emo-Blue dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Paul Hendrick
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/98.php
Requires:	%{name}

%description Emo-Blue
Theme 'Emo-Blue' by 'Paul Hendrick'. Author comment for the theme: A
theme using a cool futuristic background and nice GNOME2 icons.

%description Emo-Blue -l pl
Motyw 'Emo-Blue' autorstwa 'Paul Hendrick'. Komentarz autora do
motywu: A theme using a cool futuristic background and nice GNOME2
icons.

%package Flowers
Summary:	Theme Flowers for gdm (GNOME Display Manager)
Summary(pl):	Motyw Flowers dla gdm (Zarz±dcy ekranów GNOME)
Vendor:		Gianluca Masci
Group:		Themes
URL:		http://art.gnome.org/themes/gdm_greeter/99.php
Requires:	%{name}

%description Flowers
Theme 'Flowers' by 'Gianluca Masci'. Author comment for the theme: A
Theme with Flowers.

%description Flowers -l pl
Motyw 'Flowers' autorstwa 'Gianluca Masci'. Komentarz autora do
motywu: A Theme with Flowers.

%prep
test -d %{_builddir}/%{name}-%{version} && find %{_builddir}/%{name}-%{version}/ -type d -exec chmod 755 {} \;
test -d %{_builddir}/%{name}-%{version} && find %{_builddir}/%{name}-%{version}/ -type f -exec chmod 644 {} \;
mkdir -p %{_builddir}/%{name}-%{version}

%setup -q -c -n %{_builddir}/%{name}-%{version} -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31 -a32 -a33 -a34 -a35 -a36 -a37 -a38 -a39 -a40 -a41 -a42 -a43 -a44 -a45 -a46 -a47 -a48 -a49 -a50 -a51 -a52 -a53 -a54 -a55 -a56 -a57 -a58 -a59 -a60 -a61 -a62 -a63 -a64 -a65 -a66 -a67 -a68 -a69 -a70 -a71 -a72 -a73

cat>README<<E_O_F
This is small x-mas gift from yoshi to all PLD users, developers and
enthusiasts ;-)
Have fun and support art.gnome.org with your own creations (if you can).

Merry Christmas :)
E_O_F

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/
#
# Theme 00/73
#
# Make 'Morning_Light' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Morning_Light/
# Install 'Morning_Light' theme files
install "morning/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Morning_Light/
install "morning/help.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Morning_Light/
install "morning/morning.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Morning_Light/
install "morning/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Morning_Light/
install "morning/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Morning_Light/
install "morning/theme.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Morning_Light/
#
# Theme 01/73
#
# Make 'RedHat' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RedHat/
# Install 'RedHat' theme files
install "redhat-gdm/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RedHat/
install "redhat-gdm/help.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RedHat/
install "redhat-gdm/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RedHat/
install "redhat-gdm/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RedHat/
install "redhat-gdm/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RedHat/
install "redhat-gdm/redhat-gdm.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RedHat/
install "redhat-gdm/redhat.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RedHat/
install "redhat-gdm/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RedHat/
install "redhat-gdm/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RedHat/
#
# Theme 02/73
#
# Make 'Sea' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Sea/
# Install 'Sea' theme files
install "sea/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Sea/
install "sea/help.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Sea/
install "sea/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Sea/
install "sea/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Sea/
install "sea/sea.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Sea/
install "sea/sea.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Sea/
#
# Theme 03/73
#
# Make 'Segovia_Night' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia_Night/
# Install 'Segovia_Night' theme files
install "segovia-night/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia_Night/
install "segovia-night/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia_Night/
install "segovia-night/segovia1.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia_Night/
install "segovia-night/segovia2.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia_Night/
install "segovia-night/segovia3.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia_Night/
install "segovia-night/segovia4.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia_Night/
install "segovia-night/segovia-night.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia_Night/
install "segovia-night/segovia-night.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia_Night/
#
# Theme 04/73
#
# Make 'STGO' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/STGO/
# Install 'STGO' theme files
install "stgo/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/STGO/
install "stgo/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/STGO/
install "stgo/stgo1.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/STGO/
install "stgo/stgo2.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/STGO/
install "stgo/stgo3.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/STGO/
install "stgo/stgo4.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/STGO/
install "stgo/stgo.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/STGO/
install "stgo/stgo.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/STGO/
#
# Theme 05/73
#
# Make 'SuSE' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SuSE/
# Install 'SuSE' theme files
install "opt/gnome2/share/gdm/themes/suse-gdm/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SuSE/
install "opt/gnome2/share/gdm/themes/suse-gdm/help.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SuSE/
install "opt/gnome2/share/gdm/themes/suse-gdm/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SuSE/
install "opt/gnome2/share/gdm/themes/suse-gdm/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SuSE/
install "opt/gnome2/share/gdm/themes/suse-gdm/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SuSE/
install "opt/gnome2/share/gdm/themes/suse-gdm/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SuSE/
install "opt/gnome2/share/gdm/themes/suse-gdm/suse-gdm.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SuSE/
install "opt/gnome2/share/gdm/themes/suse-gdm/suse.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SuSE/
install "opt/gnome2/share/gdm/themes/suse-gdm/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SuSE/
#
# Theme 06/73
#
# Make 'Segovia' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia/
# Install 'Segovia' theme files
install "segovia/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia/
install "segovia/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia/
install "segovia/segovia1.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia/
install "segovia/segovia2.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia/
install "segovia/segovia3.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia/
install "segovia/segovia4.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia/
install "segovia/segovia.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia/
install "segovia/segovia.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Segovia/
#
# Theme 07/73
#
# Make 'Bluecurve' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bluecurve/
# Install 'Bluecurve' theme files
install "Bluecurve/Bluecurve.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bluecurve/
install "Bluecurve/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bluecurve/
install "Bluecurve/lightrays.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bluecurve/
install "Bluecurve/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bluecurve/
install "Bluecurve/rh_logo-header.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bluecurve/
install "Bluecurve/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bluecurve/
install "Bluecurve/shadow-bl.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bluecurve/
install "Bluecurve/shadow-b.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bluecurve/
install "Bluecurve/shadow-br.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bluecurve/
install "Bluecurve/shadow-l.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bluecurve/
install "Bluecurve/shadow-r.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bluecurve/
install "Bluecurve/shadow-tl.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bluecurve/
install "Bluecurve/shadow-t.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bluecurve/
install "Bluecurve/shadow-tr.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bluecurve/
#
# Theme 08/73
#
# Make '300-lantueno' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/300-lantueno/
# Install '300-lantueno' theme files
install "lantueno-gdm/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/300-lantueno/
install "lantueno-gdm/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/300-lantueno/
install "lantueno-gdm/lantueno.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/300-lantueno/
install "lantueno-gdm/lantueno.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/300-lantueno/
install "lantueno-gdm/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/300-lantueno/
install "lantueno-gdm/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/300-lantueno/
install "lantueno-gdm/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/300-lantueno/
install "lantueno-gdm/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/300-lantueno/
install "lantueno-gdm/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/300-lantueno/
#
# Theme 09/73
#
# Make 'XPTO' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/XPTO/
# Install 'XPTO' theme files
install "xpto/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/XPTO/
install "xpto/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/XPTO/
install "xpto/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/XPTO/
install "xpto/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/XPTO/
install "xpto/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/XPTO/
install "xpto/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/XPTO/
install "xpto/xpto_bg.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/XPTO/
install "xpto/xpto.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/XPTO/
install "xpto/xpto_shot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/XPTO/
install "xpto/xpto.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/XPTO/
install "xpto/xpt.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/XPTO/
#
# Theme 10/73
#
# Make 'Dawn' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dawn/
# Install 'Dawn' theme files
install "dawn/background.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dawn/
install "dawn/dawn.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dawn/
install "dawn/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dawn/
install "dawn/option.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dawn/
install "dawn/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dawn/
install "dawn/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dawn/
install "dawn/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dawn/
install "dawn/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dawn/
#
# Theme 11/73
#
# Make 'GDM-GlassFoot' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-GlassFoot/
# Install 'GDM-GlassFoot' theme files
install "GNOME-GlassFoot/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-GlassFoot/
install "GNOME-GlassFoot/glass.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-GlassFoot/
install "GNOME-GlassFoot/GNOME-GlassFoot.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-GlassFoot/
install "GNOME-GlassFoot/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-GlassFoot/
install "GNOME-GlassFoot/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-GlassFoot/
install "GNOME-GlassFoot/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-GlassFoot/
install "GNOME-GlassFoot/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-GlassFoot/
install "GNOME-GlassFoot/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-GlassFoot/
#
# Theme 12/73
#
# Make 'Space' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Space/
# Install 'Space' theme files
install "bisho/background.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Space/
install "bisho/Bisho.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Space/
install "bisho/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Space/
install "bisho/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Space/
install "bisho/option.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Space/
install "bisho/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Space/
install "bisho/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Space/
install "bisho/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Space/
#
# Theme 13/73
#
# Make 'Fire_Breathing_Robot' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Fire_Breathing_Robot/
# Install 'Fire_Breathing_Robot' theme files
install "flame/flames.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Fire_Breathing_Robot/
install "flame/flame.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Fire_Breathing_Robot/
install "flame/gdmbar.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Fire_Breathing_Robot/
install "flame/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Fire_Breathing_Robot/
install "flame/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Fire_Breathing_Robot/
install "flame/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Fire_Breathing_Robot/
install "flame/shadow-bl.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Fire_Breathing_Robot/
install "flame/shadow-b.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Fire_Breathing_Robot/
install "flame/shadow-br.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Fire_Breathing_Robot/
install "flame/shadow-l.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Fire_Breathing_Robot/
install "flame/shadow-r.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Fire_Breathing_Robot/
install "flame/shadow-tl.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Fire_Breathing_Robot/
install "flame/shadow-t.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Fire_Breathing_Robot/
install "flame/shadow-tr.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Fire_Breathing_Robot/
#
# Theme 14/73
#
# Make 'UnxStar' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/UnxStar/
# Install 'UnxStar' theme files
install "unxstar/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/UnxStar/
install "unxstar/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/UnxStar/
install "unxstar/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/UnxStar/
install "unxstar/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/UnxStar/
install "unxstar/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/UnxStar/
install "unxstar/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/UnxStar/
install "unxstar/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/UnxStar/
install "unxstar/unxstar.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/UnxStar/
install "unxstar/unxstar.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/UnxStar/
#
# Theme 15/73
#
# Make 'SlackGDM' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SlackGDM/
# Install 'SlackGDM' theme files
install "slackgdm/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SlackGDM/
install "slackgdm/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SlackGDM/
install "slackgdm/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SlackGDM/
install "slackgdm/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SlackGDM/
install "slackgdm/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SlackGDM/
install "slackgdm/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SlackGDM/
install "slackgdm/slackgdm.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SlackGDM/
install "slackgdm/slackgdm.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SlackGDM/
install "slackgdm/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/SlackGDM/
#
# Theme 16/73
#
# Make 'hybridFUSION' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/hybridFUSION/
# Install 'hybridFUSION' theme files
install "hybridFUSION/ConVerSion_version_Two.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/hybridFUSION/
install "hybridFUSION/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/hybridFUSION/
install "hybridFUSION/hybridFUSION.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/hybridFUSION/
install "hybridFUSION/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/hybridFUSION/
install "hybridFUSION/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/hybridFUSION/
install "hybridFUSION/shadow-bl.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/hybridFUSION/
install "hybridFUSION/shadow-b.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/hybridFUSION/
install "hybridFUSION/shadow-br.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/hybridFUSION/
install "hybridFUSION/shadow-l.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/hybridFUSION/
install "hybridFUSION/shadow-r.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/hybridFUSION/
install "hybridFUSION/shadow-tl.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/hybridFUSION/
install "hybridFUSION/shadow-t.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/hybridFUSION/
install "hybridFUSION/shadow-tr.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/hybridFUSION/
install "hybridFUSION/skowals.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/hybridFUSION/
#
# Theme 17/73
#
# Make 'Barcelona' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Barcelona/
# Install 'Barcelona' theme files
install "barna/barna-desconectar.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Barcelona/
install "barna/barna.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Barcelona/
install "barna/barna-opciones.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Barcelona/
install "barna/barna-sesion.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Barcelona/
install "barna/barna-sistema.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Barcelona/
install "barna/barna.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Barcelona/
install "barna/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Barcelona/
install "barna/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Barcelona/
#
# Theme 18/73
#
# Make 'Valladolid' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Valladolid/
# Install 'Valladolid' theme files
install "valladolid/ava-desconectar.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Valladolid/
install "valladolid/ava-opcion.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Valladolid/
install "valladolid/ava-sesion.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Valladolid/
install "valladolid/ava-sistema.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Valladolid/
install "valladolid/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Valladolid/
install "valladolid/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Valladolid/
install "valladolid/valladolid.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Valladolid/
install "valladolid/valladolid.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Valladolid/
#
# Theme 19/73
#
# Make 'Murcia' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Murcia/
# Install 'Murcia' theme files
install "murcia/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Murcia/
install "murcia/murcia-desconectar.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Murcia/
install "murcia/murcia.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Murcia/
install "murcia/murcia-opciones.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Murcia/
install "murcia/murcia-sesion.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Murcia/
install "murcia/murcia-sistema.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Murcia/
install "murcia/murcia.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Murcia/
install "murcia/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Murcia/
#
# Theme 20/73
#
# Make 'Leon' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Leon/
# Install 'Leon' theme files
install "leon/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Leon/
install "leon/leon-desconectar.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Leon/
install "leon/leon.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Leon/
install "leon/leon-opciones.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Leon/
install "leon/leon-sesion.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Leon/
install "leon/leon-sistema.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Leon/
install "leon/leon.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Leon/
install "leon/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Leon/
#
# Theme 21/73
#
# Make 'Gentoo_Emergence' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gentoo_Emergence/
# Install 'Gentoo_Emergence' theme files
install "gentoo-emergence/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gentoo_Emergence/
install "gentoo-emergence/gentoo-emergence.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gentoo_Emergence/
install "gentoo-emergence/gentoo-emergence.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gentoo_Emergence/
install "gentoo-emergence/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gentoo_Emergence/
install "gentoo-emergence/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gentoo_Emergence/
install "gentoo-emergence/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gentoo_Emergence/
install "gentoo-emergence/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gentoo_Emergence/
install "gentoo-emergence/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gentoo_Emergence/
install "gentoo-emergence/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gentoo_Emergence/
#
# Theme 22/73
#
# Make 'FreeBSD_The_Power_of_Serve' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/
# Install 'FreeBSD_The_Power_of_Serve' theme files
install "FreeBSD/FreeBSD.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/
install "FreeBSD/FreeBSD.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/
install "FreeBSD/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/
install "FreeBSD/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/
install "FreeBSD/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/
install "FreeBSD/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/
install "FreeBSD/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/
install "FreeBSD/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/
install "FreeBSD/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/
#
# Theme 23/73
#
# Make 'Daybreak' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Daybreak/
# Install 'Daybreak' theme files
install "daybreak/daybreak.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Daybreak/
install "daybreak/daybreak.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Daybreak/
install "daybreak/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Daybreak/
install "daybreak/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Daybreak/
install "daybreak/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Daybreak/
install "daybreak/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Daybreak/
install "daybreak/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Daybreak/
install "daybreak/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Daybreak/
install "daybreak/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Daybreak/
#
# Theme 24/73
#
# Make 'Bijou' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bijou/
# Install 'Bijou' theme files
install "bijou/background.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bijou/
install "bijou/bijou.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bijou/
install "bijou/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bijou/
install "bijou/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bijou/
install "bijou/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bijou/
install "bijou/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bijou/
install "bijou/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bijou/
install "bijou/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bijou/
#
# Theme 25/73
#
# Make 'Stop_TCPA' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Stop_TCPA/
# Install 'Stop_TCPA' theme files
install "tcpa/background.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Stop_TCPA/
install "tcpa/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Stop_TCPA/
install "tcpa/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Stop_TCPA/
install "tcpa/option.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Stop_TCPA/
install "tcpa/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Stop_TCPA/
install "tcpa/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Stop_TCPA/
install "tcpa/tcpa.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Stop_TCPA/
#
# Theme 26/73
#
# Make 'Open_Source_Initiative' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Open_Source_Initiative/
# Install 'Open_Source_Initiative' theme files
install "OpenSource/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Open_Source_Initiative/
install "OpenSource/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Open_Source_Initiative/
install "OpenSource/open_source.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Open_Source_Initiative/
install "OpenSource/open_source.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Open_Source_Initiative/
install "OpenSource/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Open_Source_Initiative/
install "OpenSource/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Open_Source_Initiative/
install "OpenSource/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Open_Source_Initiative/
install "OpenSource/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Open_Source_Initiative/
install "OpenSource/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Open_Source_Initiative/
#
# Theme 27/73
#
# Make 'FreeBSDarth' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSDarth/
# Install 'FreeBSDarth' theme files
install "FreeBSDarth/FreeBSDarth.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSDarth/
install "FreeBSDarth/FreeBSDarth.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSDarth/
install "FreeBSDarth/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSDarth/
install "FreeBSDarth/help.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSDarth/
install "FreeBSDarth/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSDarth/
install "FreeBSDarth/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSDarth/
install "FreeBSDarth/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/FreeBSDarth/
#
# Theme 28/73
#
# Make 'Penguin_Computing' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Penguin_Computing/
# Install 'Penguin_Computing' theme files
install "penguin/background.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Penguin_Computing/
install "penguin/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Penguin_Computing/
install "penguin/galikynes.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Penguin_Computing/
install "penguin/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Penguin_Computing/
install "penguin/option.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Penguin_Computing/
install "penguin/penguin.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Penguin_Computing/
install "penguin/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Penguin_Computing/
install "penguin/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Penguin_Computing/
#
# Theme 29/73
#
# Make 'Knoke' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Knoke/
# Install 'Knoke' theme files
install "knoke/back.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Knoke/
install "knoke/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Knoke/
install "knoke/knoke.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Knoke/
install "knoke/knoke.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Knoke/
install "knoke/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Knoke/
install "knoke/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Knoke/
install "knoke/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Knoke/
install "knoke/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Knoke/
install "knoke/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Knoke/
#
# Theme 30/73
#
# Make 'The_Dark_Crystal' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/The_Dark_Crystal/
# Install 'The_Dark_Crystal' theme files
install "darkcrystal/background.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/The_Dark_Crystal/
install "darkcrystal/darkcrystal.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/The_Dark_Crystal/
install "darkcrystal/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/The_Dark_Crystal/
install "darkcrystal/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/The_Dark_Crystal/
install "darkcrystal/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/The_Dark_Crystal/
install "darkcrystal/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/The_Dark_Crystal/
install "darkcrystal/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/The_Dark_Crystal/
#
# Theme 31/73
#
# Make 'Gnome_Chile' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gnome_Chile/
# Install 'Gnome_Chile' theme files
install "gnome-chile/fondo.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gnome_Chile/
install "gnome-chile/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gnome_Chile/
install "gnome-chile/gnome-chile.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gnome_Chile/
install "gnome-chile/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gnome_Chile/
install "gnome-chile/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gnome_Chile/
install "gnome-chile/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gnome_Chile/
install "gnome-chile/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gnome_Chile/
install "gnome-chile/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gnome_Chile/
install "gnome-chile/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gnome_Chile/
#
# Theme 32/73
#
# Make 'Glassy' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Glassy/
# Install 'Glassy' theme files
install "Glassy/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Glassy/
install "Glassy/glassy.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Glassy/
install "Glassy/glassy.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Glassy/
install "Glassy/help.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Glassy/
install "Glassy/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Glassy/
install "Glassy/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Glassy/
install "Glassy/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Glassy/
install "Glassy/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Glassy/
install "Glassy/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Glassy/
#
# Theme 33/73
#
# Make 'Machu_Picchu' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Machu_Picchu/
# Install 'Machu_Picchu' theme files
install "Machu Picchu/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Machu_Picchu/
install "Machu Picchu/Machu Picchu.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Machu_Picchu/
install "Machu Picchu/MP-ledge-bg.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Machu_Picchu/
install "Machu Picchu/MP-tall-options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Machu_Picchu/
install "Machu Picchu/MP-tall-quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Machu_Picchu/
install "Machu Picchu/MP-tall-session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Machu_Picchu/
install "Machu Picchu/MP-tall-system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Machu_Picchu/
install "Machu Picchu/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Machu_Picchu/
#
# Theme 34/73
#
# Make 'RightVision' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RightVision/
# Install 'RightVision' theme files
install "RV/background.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RightVision/
install "RV/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RightVision/
install "RV/logorv.gif" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RightVision/
install "RV/oeil1.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RightVision/
install "RV/oeil2.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RightVision/
install "RV/oeil3.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RightVision/
install "RV/oeil4.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RightVision/
install "RV/rv.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RightVision/
install "RV/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/RightVision/
#
# Theme 35/73
#
# Make 'La_Bisbal_dEmpord_nevada' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/
# Install 'La_Bisbal_dEmpord_nevada' theme files
install "labisbal/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/
install "labisbal/labisbal-desconectar.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/
install "labisbal/labisbal.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/
install "labisbal/labisbal-opcions.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/
install "labisbal/labisbal-sessio.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/
install "labisbal/labisbal-sistema.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/
install "labisbal/labisbal.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/
install "labisbal/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/
#
# Theme 36/73
#
# Make 'Falling_Angel' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Falling_Angel/
# Install 'Falling_Angel' theme files
install "falling-angel/falling-angel.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Falling_Angel/
install "falling-angel/falling-angel-shot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Falling_Angel/
install "falling-angel/falling-angel.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Falling_Angel/
install "falling-angel/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Falling_Angel/
install "falling-angel/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Falling_Angel/
install "falling-angel/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Falling_Angel/
install "falling-angel/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Falling_Angel/
install "falling-angel/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Falling_Angel/
install "falling-angel/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Falling_Angel/
#
# Theme 37/73
#
# Make 'Hantzley' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Hantzley/
# Install 'Hantzley' theme files
install "Hantzley/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Hantzley/
install "Hantzley/hantzley.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Hantzley/
install "Hantzley/hantzley.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Hantzley/
install "Hantzley/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Hantzley/
install "Hantzley/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Hantzley/
install "Hantzley/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Hantzley/
install "Hantzley/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Hantzley/
install "Hantzley/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Hantzley/
install "Hantzley/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Hantzley/
#
# Theme 38/73
#
# Make 'Mozi' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mozi/
# Install 'Mozi' theme files
install "Mozi/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mozi/
install "Mozi/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mozi/
install "Mozi/mozilla.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mozi/
install "Mozi/option.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mozi/
install "Mozi/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mozi/
install "Mozi/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mozi/
install "Mozi/soho.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mozi/
install "Mozi/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mozi/
#
# Theme 39/73
#
# Make 'Todmorden' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Todmorden/
# Install 'Todmorden' theme files
install "Todmorden/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Todmorden/
install "Todmorden/help.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Todmorden/
install "Todmorden/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Todmorden/
install "Todmorden/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Todmorden/
install "Todmorden/todmorden.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Todmorden/
install "Todmorden/todmorden.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Todmorden/
#
# Theme 40/73
#
# Make 'Hunter' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Hunter/
# Install 'Hunter' theme files
install "hunter/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Hunter/
install "hunter/help.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Hunter/
install "hunter/hunter.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Hunter/
install "hunter/hunter.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Hunter/
install "hunter/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Hunter/
install "hunter/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Hunter/
#
# Theme 41/73
#
# Make 'GDM-Mosaic' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-Mosaic/
# Install 'GDM-Mosaic' theme files
install "Mosaic/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-Mosaic/
install "Mosaic/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-Mosaic/
install "Mosaic/Mosaic.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-Mosaic/
install "Mosaic/Mosaic.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-Mosaic/
install "Mosaic/option.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-Mosaic/
install "Mosaic/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-Mosaic/
install "Mosaic/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-Mosaic/
install "Mosaic/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/GDM-Mosaic/
#
# Theme 42/73
#
# Make 'KDE_Crystal' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/KDE_Crystal/
# Install 'KDE_Crystal' theme files
install "crystal_gdm/background.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/KDE_Crystal/
install "crystal_gdm/crystal.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/KDE_Crystal/
install "crystal_gdm/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/KDE_Crystal/
install "crystal_gdm/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/KDE_Crystal/
install "crystal_gdm/halt.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/KDE_Crystal/
install "crystal_gdm/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/KDE_Crystal/
install "crystal_gdm/reboot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/KDE_Crystal/
install "crystal_gdm/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/KDE_Crystal/
install "crystal_gdm/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/KDE_Crystal/
#
# Theme 43/73
#
# Make 'Crystal_Rose' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal_Rose/
# Install 'Crystal_Rose' theme files
install "crystal-rose/crystal-rose.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal_Rose/
install "crystal-rose/crystal-rose.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal_Rose/
install "crystal-rose/crystal-rose-screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal_Rose/
install "crystal-rose/crystal-rose.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal_Rose/
install "crystal-rose/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal_Rose/
install "crystal-rose/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal_Rose/
install "crystal-rose.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal_Rose/
#
# Theme 44/73
#
# Make 'Devils_Candy' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Devils_Candy/
# Install 'Devils_Candy' theme files
install "DevilsCandy/background.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Devils_Candy/
install "DevilsCandy/ball.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Devils_Candy/
install "DevilsCandy/devil.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Devils_Candy/
install "DevilsCandy/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Devils_Candy/
install "DevilsCandy/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Devils_Candy/
install "DevilsCandy/option.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Devils_Candy/
install "DevilsCandy/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Devils_Candy/
install "DevilsCandy/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Devils_Candy/
install "DevilsCandy/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Devils_Candy/
#
# Theme 45/73
#
# Make 'Synergy' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Synergy/
# Install 'Synergy' theme files
install "Synergy/background.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Synergy/
install "Synergy/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Synergy/
install "Synergy/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Synergy/
install "Synergy/halt.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Synergy/
install "Synergy/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Synergy/
install "Synergy/reboot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Synergy/
install "Synergy/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Synergy/
install "Synergy/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Synergy/
install "Synergy/theme.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Synergy/
#
# Theme 46/73
#
# Make 'Cubic_Linux_and_Gnome' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/
# Install 'Cubic_Linux_and_Gnome' theme files
install "Cubic_Linux_Gnome/background.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/
install "Cubic_Linux_Gnome/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/
install "Cubic_Linux_Gnome/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/
install "Cubic_Linux_Gnome/halt.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/
install "Cubic_Linux_Gnome/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/
install "Cubic_Linux_Gnome/reboot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/
install "Cubic_Linux_Gnome/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/
install "Cubic_Linux_Gnome/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/
install "Cubic_Linux_Gnome/theme.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cubic_Linux_and_Gnome/
#
# Theme 47/73
#
# Make 'Butterfly' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Butterfly/
# Install 'Butterfly' theme files
install "butterfly/bfly.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Butterfly/
install "butterfly/butterfly.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Butterfly/
install "butterfly/butterfly_tahoma.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Butterfly/
install "butterfly/butterfly.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Butterfly/
install "butterfly/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Butterfly/
install "butterfly/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Butterfly/
install "butterfly/option.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Butterfly/
install "butterfly/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Butterfly/
install "butterfly/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Butterfly/
#
# Theme 48/73
#
# Make 'Mirrored' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mirrored/
# Install 'Mirrored' theme files
install "mirrored-theme/background.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mirrored/
install "mirrored-theme/COPYING" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mirrored/
install "mirrored-theme/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mirrored/
install "mirrored-theme/head1.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mirrored/
install "mirrored-theme/head3.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mirrored/
install "mirrored-theme/head4.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mirrored/
install "mirrored-theme/head5.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mirrored/
install "mirrored-theme/mirrored.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mirrored/
install "mirrored-theme/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mirrored/
install "mirrored-theme/sys.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mirrored/
#
# Theme 49/73
#
# Make 'Delicious' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Delicious/
# Install 'Delicious' theme files
install "delicious-theme/delicious.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Delicious/
install "delicious-theme/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Delicious/
install "delicious-theme/head1.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Delicious/
install "delicious-theme/mampf.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Delicious/
install "delicious-theme/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Delicious/
install "delicious-theme/screenshot-small.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Delicious/
install "delicious-theme/sys.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Delicious/
#
# Theme 50/73
#
# Make 'Blue_Slack_GDM' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blue_Slack_GDM/
# Install 'Blue_Slack_GDM' theme files
install "blueslackGDM/blueslack.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blue_Slack_GDM/
install "blueslackGDM/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blue_Slack_GDM/
install "blueslackGDM/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blue_Slack_GDM/
install "blueslackGDM/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blue_Slack_GDM/
install "blueslackGDM/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blue_Slack_GDM/
install "blueslackGDM/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blue_Slack_GDM/
install "blueslackGDM/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blue_Slack_GDM/
install "blueslackGDM/slackblue.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blue_Slack_GDM/
install "blueslackGDM/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blue_Slack_GDM/
#
# Theme 51/73
#
# Make 'Dreaming_Alien' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dreaming_Alien/
# Install 'Dreaming_Alien' theme files
install "usr/share/gdm/themes/dreaming-alien/background.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dreaming_Alien/
install "usr/share/gdm/themes/dreaming-alien/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dreaming_Alien/
install "usr/share/gdm/themes/dreaming-alien/dreaming-alien.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dreaming_Alien/
install "usr/share/gdm/themes/dreaming-alien/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dreaming_Alien/
install "usr/share/gdm/themes/dreaming-alien/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dreaming_Alien/
install "usr/share/gdm/themes/dreaming-alien/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dreaming_Alien/
install "usr/share/gdm/themes/dreaming-alien/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dreaming_Alien/
install "usr/share/gdm/themes/dreaming-alien/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dreaming_Alien/
#
# Theme 52/73
#
# Make 'gcr-ddlm' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/gcr-ddlm/
# Install 'gcr-ddlm' theme files
install "gcr-ddlm/gcr-ddlm.background.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/gcr-ddlm/
install "gcr-ddlm/gcr-ddlm.background.screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/gcr-ddlm/
install "gcr-ddlm/gcr-ddlm.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/gcr-ddlm/
install "gcr-ddlm/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/gcr-ddlm/
install "gcr-ddlm/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/gcr-ddlm/
install "gcr-ddlm/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/gcr-ddlm/
install "gcr-ddlm/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/gcr-ddlm/
install "gcr-ddlm/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/gcr-ddlm/
#
# Theme 53/73
#
# Make 'Gentoo_Cow' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gentoo_Cow/
# Install 'Gentoo_Cow' theme files
install "gentoo-cow/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gentoo_Cow/
install "gentoo-cow/gentoo-cow-alpha.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gentoo_Cow/
install "gentoo-cow/gentoo-cow.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gentoo_Cow/
install "gentoo-cow/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gentoo_Cow/
install "gentoo-cow/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gentoo_Cow/
#
# Theme 54/73
#
# Make 'Just_BSD' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Just_BSD/
# Install 'Just_BSD' theme files
install "BSD/BSD.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Just_BSD/
install "BSD/BSD.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Just_BSD/
install "BSD/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Just_BSD/
install "BSD/icon.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Just_BSD/
install "BSD/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Just_BSD/
install "BSD/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Just_BSD/
#
# Theme 55/73
#
# Make 'pixelGDM' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/pixelGDM/
# Install 'pixelGDM' theme files
install "pixelGDM/background.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/pixelGDM/
install "pixelGDM/disconnect_over.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/pixelGDM/
install "pixelGDM/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/pixelGDM/
install "pixelGDM/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/pixelGDM/
install "pixelGDM/language_over.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/pixelGDM/
install "pixelGDM/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/pixelGDM/
install "pixelGDM/pixelGDM.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/pixelGDM/
install "pixelGDM/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/pixelGDM/
install "pixelGDM/screenshot-small.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/pixelGDM/
install "pixelGDM/session_over.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/pixelGDM/
install "pixelGDM/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/pixelGDM/
install "pixelGDM/shutdown_over.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/pixelGDM/
install "pixelGDM/shutdown.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/pixelGDM/
install "pixelGDM/system_over.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/pixelGDM/
install "pixelGDM/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/pixelGDM/
#
# Theme 56/73
#
# Make 'Red_Leaves' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Red_Leaves/
# Install 'Red_Leaves' theme files
install "leaves/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Red_Leaves/
install "leaves/leaves.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Red_Leaves/
install "leaves/leaves-screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Red_Leaves/
install "leaves/leaves.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Red_Leaves/
install "leaves/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Red_Leaves/
#
# Theme 57/73
#
# Make 'Mono_Metal' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mono_Metal/
# Install 'Mono_Metal' theme files
install "mono-metal/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mono_Metal/
install "mono-metal/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mono_Metal/
install "mono-metal/metal.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mono_Metal/
install "mono-metal/mono_metal.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mono_Metal/
install "mono-metal/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mono_Metal/
install "mono-metal/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mono_Metal/
install "mono-metal/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mono_Metal/
install "mono-metal/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Mono_Metal/
#
# Theme 58/73
#
# Make 'Gdm_Dropline' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gdm_Dropline/
# Install 'Gdm_Dropline' theme files
install "gdm-dropline/dropline-blue.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gdm_Dropline/
install "gdm-dropline/dropline-blue.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gdm_Dropline/
install "gdm-dropline/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gdm_Dropline/
install "gdm-dropline/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gdm_Dropline/
install "gdm-dropline/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gdm_Dropline/
install "gdm-dropline/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gdm_Dropline/
install "gdm-dropline/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gdm_Dropline/
install "gdm-dropline/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gdm_Dropline/
install "gdm-dropline/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Gdm_Dropline/
#
# Theme 59/73
#
# Make 'Bee_at_Work' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bee_at_Work/
# Install 'Bee_at_Work' theme files
install "BeeAtWork/background.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bee_at_Work/
install "BeeAtWork/BeeAtWork.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bee_at_Work/
install "BeeAtWork/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bee_at_Work/
install "BeeAtWork/help.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bee_at_Work/
install "BeeAtWork/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bee_at_Work/
install "BeeAtWork/theme.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Bee_at_Work/
#
# Theme 60/73
#
# Make 'LinuxTux' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/LinuxTux/
# Install 'LinuxTux' theme files
install "linuxtux/background.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/LinuxTux/
install "linuxtux/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/LinuxTux/
install "linuxtux/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/LinuxTux/
install "linuxtux/option.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/LinuxTux/
install "linuxtux/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/LinuxTux/
install "linuxtux/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/LinuxTux/
install "linuxtux/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/LinuxTux/
install "linuxtux/tux.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/LinuxTux/
install "linuxtux/tux.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/LinuxTux/
#
# Theme 61/73
#
# Make 'Taipei' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Taipei/
# Install 'Taipei' theme files
install "Taipei/background.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Taipei/
install "Taipei/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Taipei/
install "Taipei/help.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Taipei/
install "Taipei/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Taipei/
install "Taipei/Taipei.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Taipei/
install "Taipei/theme.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Taipei/
#
# Theme 62/73
#
# Make 'Odysseus' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Odysseus/
# Install 'Odysseus' theme files
install "odysseus/background.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Odysseus/
install "odysseus/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Odysseus/
install "odysseus/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Odysseus/
install "odysseus/Odysseus.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Odysseus/
install "odysseus/option.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Odysseus/
install "odysseus/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Odysseus/
install "odysseus/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Odysseus/
install "odysseus/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Odysseus/
#
# Theme 63/73
#
# Make 'Kinkakuji' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Kinkakuji/
# Install 'Kinkakuji' theme files
install "kinkakuji/background.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Kinkakuji/
install "kinkakuji/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Kinkakuji/
install "kinkakuji/help.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Kinkakuji/
install "kinkakuji/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Kinkakuji/
install "kinkakuji/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Kinkakuji/
install "kinkakuji/theme.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Kinkakuji/
#
# Theme 64/73
#
# Make 'Milk' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Milk/
# Install 'Milk' theme files
install "milk/background.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Milk/
install "milk/background.svg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Milk/
install "milk/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Milk/
install "milk/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Milk/
install "milk/gnome-logo.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Milk/
install "milk/milk.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Milk/
install "milk/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Milk/
install "milk/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Milk/
install "milk/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Milk/
install "milk/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Milk/
#
# Theme 65/73
#
# Make 'Crop_Circles' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
# Install 'Crop_Circles' theme files
install "./cropcircles/background.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
install "./cropcircles/Bottombar.svg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
install "./cropcircles/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
install "./cropcircles/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
install "./cropcircles/gnome-logo.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
install "./cropcircles/halt.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
install "./cropcircles/lang.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
install "./cropcircles/List.svg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
install "./cropcircles/Login.svg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
install "./cropcircles/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
install "./cropcircles/readme" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
install "./cropcircles/reboot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
install "./cropcircles/roundrect.svg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
install "./cropcircles/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
install "./cropcircles/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
install "./cropcircles/signs.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
install "./cropcircles/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
install "./cropcircles/Topbar.svg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crop_Circles/
#
# Theme 66/73
#
# Make 'Angel' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Angel/
# Install 'Angel' theme files
install "Angel/angel.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Angel/
install "Angel/angel.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Angel/
install "Angel/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Angel/
install "Angel/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Angel/
install "Angel/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Angel/
install "Angel/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Angel/
install "Angel/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Angel/
install "Angel/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Angel/
install "Angel/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Angel/
#
# Theme 67/73
#
# Make 'Blueish' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blueish/
# Install 'Blueish' theme files
install "bluish-gdm/bluish-gdm.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blueish/
install "bluish-gdm/bluish.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blueish/
install "bluish-gdm/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blueish/
install "bluish-gdm/help.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blueish/
install "bluish-gdm/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blueish/
install "bluish-gdm/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blueish/
install "bluish-gdm/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blueish/
install "bluish-gdm/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blueish/
install "bluish-gdm/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Blueish/
#
# Theme 68/73
#
# Make 'Cracked_Windows' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cracked_Windows/
# Install 'Cracked_Windows' theme files
install "cracked-windows/cracked-windows.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cracked_Windows/
install "cracked-windows/cracked-windows.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cracked_Windows/
install "cracked-windows/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cracked_Windows/
install "cracked-windows/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cracked_Windows/
install "cracked-windows/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cracked_Windows/
install "cracked-windows/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cracked_Windows/
install "cracked-windows/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cracked_Windows/
install "cracked-windows/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Cracked_Windows/
#
# Theme 69/73
#
# Make 'Crystal' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal/
# Install 'Crystal' theme files
install "crystal/background.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal/
install "crystal/Crystal.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal/
install "crystal/disconnect.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal/
install "crystal/galikynes.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal/
install "crystal/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal/
install "crystal/option.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal/
install "crystal/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal/
install "crystal/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal/
install "crystal/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Crystal/
#
# Theme 70/73
#
# Make 'Dart_Frog' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dart_Frog/
# Install 'Dart_Frog' theme files
install "dartfrog/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dart_Frog/
install "dartfrog/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dart_Frog/
install "dartfrog/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dart_Frog/
install "dartfrog/pitcherplant.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dart_Frog/
install "dartfrog/pitcherplant.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dart_Frog/
install "dartfrog/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dart_Frog/
install "dartfrog/screenshot.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dart_Frog/
install "dartfrog/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dart_Frog/
install "dartfrog/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Dart_Frog/
#
# Theme 71/73
#
# Make 'DumbCloud' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/DumbCloud/
# Install 'DumbCloud' theme files
install "dumbcloud/cloud2.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/DumbCloud/
install "dumbcloud/dumbcloud.svg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/DumbCloud/
install "dumbcloud/dumbcloud.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/DumbCloud/
install "dumbcloud/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/DumbCloud/
install "dumbcloud/help.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/DumbCloud/
install "dumbcloud/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/DumbCloud/
install "dumbcloud/test2.svg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/DumbCloud/
#
# Theme 72/73
#
# Make 'Emo-Blue' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Emo-Blue/
# Install 'Emo-Blue' theme files
install "emo-blue/emo-blue.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Emo-Blue/
install "emo-blue/emo-blue.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Emo-Blue/
install "emo-blue/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Emo-Blue/
install "emo-blue/language.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Emo-Blue/
install "emo-blue/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Emo-Blue/
install "emo-blue/quit.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Emo-Blue/
install "emo-blue/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Emo-Blue/
install "emo-blue/session.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Emo-Blue/
install "emo-blue/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Emo-Blue/
#
# Theme 73/73
#
# Make 'Flowers' theme directory
install -d $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Flowers/
# Install 'Flowers' theme files
install "flowers/background.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Flowers/
install "flowers/flowers.xml" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Flowers/
install "flowers/GdmGreeterTheme.desktop" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Flowers/
install "flowers/help.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Flowers/
install "flowers/options.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Flowers/
install "flowers/screenshot.jpg" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Flowers/
install "flowers/system.png" $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/Flowers/

%files
%defattr(644,root,root,755)
%doc README

#
# Theme 00/73
#
%files Morning_Light
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Morning_Light/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Morning_Light/help.png
%{_datadir}/gdm/themes/Morning_Light/morning.jpg
%{_datadir}/gdm/themes/Morning_Light/options.png
%{_datadir}/gdm/themes/Morning_Light/screenshot.png
%{_datadir}/gdm/themes/Morning_Light/theme.xml

#
# Theme 01/73
#
%files RedHat
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/RedHat/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/RedHat/help.png
%{_datadir}/gdm/themes/RedHat/language.png
%{_datadir}/gdm/themes/RedHat/options.png
%{_datadir}/gdm/themes/RedHat/quit.png
%{_datadir}/gdm/themes/RedHat/redhat-gdm.xml
%{_datadir}/gdm/themes/RedHat/redhat.png
%{_datadir}/gdm/themes/RedHat/screenshot.png
%{_datadir}/gdm/themes/RedHat/system.png

#
# Theme 02/73
#
%files Sea
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Sea/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Sea/help.png
%{_datadir}/gdm/themes/Sea/options.png
%{_datadir}/gdm/themes/Sea/screenshot.jpg
%{_datadir}/gdm/themes/Sea/sea.jpg
%{_datadir}/gdm/themes/Sea/sea.xml

#
# Theme 03/73
#
%files Segovia_Night
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Segovia_Night/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Segovia_Night/screenshot.jpg
%{_datadir}/gdm/themes/Segovia_Night/segovia1.jpg
%{_datadir}/gdm/themes/Segovia_Night/segovia2.jpg
%{_datadir}/gdm/themes/Segovia_Night/segovia3.jpg
%{_datadir}/gdm/themes/Segovia_Night/segovia4.jpg
%{_datadir}/gdm/themes/Segovia_Night/segovia-night.jpg
%{_datadir}/gdm/themes/Segovia_Night/segovia-night.xml

#
# Theme 04/73
#
%files STGO
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/STGO/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/STGO/screenshot.jpg
%{_datadir}/gdm/themes/STGO/stgo1.jpg
%{_datadir}/gdm/themes/STGO/stgo2.jpg
%{_datadir}/gdm/themes/STGO/stgo3.jpg
%{_datadir}/gdm/themes/STGO/stgo4.jpg
%{_datadir}/gdm/themes/STGO/stgo.jpg
%{_datadir}/gdm/themes/STGO/stgo.xml

#
# Theme 05/73
#
%files SuSE
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/SuSE/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/SuSE/help.png
%{_datadir}/gdm/themes/SuSE/language.png
%{_datadir}/gdm/themes/SuSE/options.png
%{_datadir}/gdm/themes/SuSE/quit.png
%{_datadir}/gdm/themes/SuSE/screenshot.png
%{_datadir}/gdm/themes/SuSE/suse-gdm.xml
%{_datadir}/gdm/themes/SuSE/suse.png
%{_datadir}/gdm/themes/SuSE/system.png

#
# Theme 06/73
#
%files Segovia
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Segovia/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Segovia/screenshot.jpg
%{_datadir}/gdm/themes/Segovia/segovia1.jpg
%{_datadir}/gdm/themes/Segovia/segovia2.jpg
%{_datadir}/gdm/themes/Segovia/segovia3.jpg
%{_datadir}/gdm/themes/Segovia/segovia4.jpg
%{_datadir}/gdm/themes/Segovia/segovia.jpg
%{_datadir}/gdm/themes/Segovia/segovia.xml

#
# Theme 07/73
#
%files Bluecurve
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Bluecurve/Bluecurve.xml
%{_datadir}/gdm/themes/Bluecurve/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Bluecurve/lightrays.png
%{_datadir}/gdm/themes/Bluecurve/options.png
%{_datadir}/gdm/themes/Bluecurve/rh_logo-header.png
%{_datadir}/gdm/themes/Bluecurve/screenshot.png
%{_datadir}/gdm/themes/Bluecurve/shadow-bl.png
%{_datadir}/gdm/themes/Bluecurve/shadow-b.png
%{_datadir}/gdm/themes/Bluecurve/shadow-br.png
%{_datadir}/gdm/themes/Bluecurve/shadow-l.png
%{_datadir}/gdm/themes/Bluecurve/shadow-r.png
%{_datadir}/gdm/themes/Bluecurve/shadow-tl.png
%{_datadir}/gdm/themes/Bluecurve/shadow-t.png
%{_datadir}/gdm/themes/Bluecurve/shadow-tr.png

#
# Theme 08/73
#
%files 300-lantueno
%defattr(644,root,root,755)
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
# Theme 09/73
#
%files XPTO
%defattr(644,root,root,755)
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

#
# Theme 10/73
#
%files Dawn
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Dawn/background.jpg
%{_datadir}/gdm/themes/Dawn/dawn.xml
%{_datadir}/gdm/themes/Dawn/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Dawn/option.png
%{_datadir}/gdm/themes/Dawn/quit.png
%{_datadir}/gdm/themes/Dawn/screenshot.jpg
%{_datadir}/gdm/themes/Dawn/session.png
%{_datadir}/gdm/themes/Dawn/system.png

#
# Theme 11/73
#
%files GDM-GlassFoot
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/GDM-GlassFoot/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/GDM-GlassFoot/glass.png
%{_datadir}/gdm/themes/GDM-GlassFoot/GNOME-GlassFoot.xml
%{_datadir}/gdm/themes/GDM-GlassFoot/language.png
%{_datadir}/gdm/themes/GDM-GlassFoot/quit.png
%{_datadir}/gdm/themes/GDM-GlassFoot/screenshot.png
%{_datadir}/gdm/themes/GDM-GlassFoot/session.png
%{_datadir}/gdm/themes/GDM-GlassFoot/system.png

#
# Theme 12/73
#
%files Space
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Space/background.png
%{_datadir}/gdm/themes/Space/Bisho.xml
%{_datadir}/gdm/themes/Space/disconnect.png
%{_datadir}/gdm/themes/Space/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Space/option.png
%{_datadir}/gdm/themes/Space/screenshot.png
%{_datadir}/gdm/themes/Space/session.png
%{_datadir}/gdm/themes/Space/system.png

#
# Theme 13/73
#
%files Fire_Breathing_Robot
%defattr(644,root,root,755)
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
# Theme 14/73
#
%files UnxStar
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/UnxStar/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/UnxStar/language.png
%{_datadir}/gdm/themes/UnxStar/options.png
%{_datadir}/gdm/themes/UnxStar/quit.png
%{_datadir}/gdm/themes/UnxStar/screenshot.png
%{_datadir}/gdm/themes/UnxStar/session.png
%{_datadir}/gdm/themes/UnxStar/system.png
%{_datadir}/gdm/themes/UnxStar/unxstar.png
%{_datadir}/gdm/themes/UnxStar/unxstar.xml

#
# Theme 15/73
#
%files SlackGDM
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/SlackGDM/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/SlackGDM/language.png
%{_datadir}/gdm/themes/SlackGDM/options.png
%{_datadir}/gdm/themes/SlackGDM/quit.png
%{_datadir}/gdm/themes/SlackGDM/screenshot.png
%{_datadir}/gdm/themes/SlackGDM/session.png
%{_datadir}/gdm/themes/SlackGDM/slackgdm.png
%{_datadir}/gdm/themes/SlackGDM/slackgdm.xml
%{_datadir}/gdm/themes/SlackGDM/system.png

#
# Theme 16/73
#
%files hybridFUSION
%defattr(644,root,root,755)
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
# Theme 17/73
#
%files Barcelona
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Barcelona/barna-desconectar.jpg
%{_datadir}/gdm/themes/Barcelona/barna.jpg
%{_datadir}/gdm/themes/Barcelona/barna-opciones.jpg
%{_datadir}/gdm/themes/Barcelona/barna-sesion.jpg
%{_datadir}/gdm/themes/Barcelona/barna-sistema.jpg
%{_datadir}/gdm/themes/Barcelona/barna.xml
%{_datadir}/gdm/themes/Barcelona/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Barcelona/screenshot.jpg

#
# Theme 18/73
#
%files Valladolid
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Valladolid/ava-desconectar.jpg
%{_datadir}/gdm/themes/Valladolid/ava-opcion.jpg
%{_datadir}/gdm/themes/Valladolid/ava-sesion.jpg
%{_datadir}/gdm/themes/Valladolid/ava-sistema.jpg
%{_datadir}/gdm/themes/Valladolid/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Valladolid/screenshot.jpg
%{_datadir}/gdm/themes/Valladolid/valladolid.jpg
%{_datadir}/gdm/themes/Valladolid/valladolid.xml

#
# Theme 19/73
#
%files Murcia
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Murcia/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Murcia/murcia-desconectar.jpg
%{_datadir}/gdm/themes/Murcia/murcia.jpg
%{_datadir}/gdm/themes/Murcia/murcia-opciones.jpg
%{_datadir}/gdm/themes/Murcia/murcia-sesion.jpg
%{_datadir}/gdm/themes/Murcia/murcia-sistema.jpg
%{_datadir}/gdm/themes/Murcia/murcia.xml
%{_datadir}/gdm/themes/Murcia/screenshot.jpg

#
# Theme 20/73
#
%files Leon
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Leon/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Leon/leon-desconectar.jpg
%{_datadir}/gdm/themes/Leon/leon.jpg
%{_datadir}/gdm/themes/Leon/leon-opciones.jpg
%{_datadir}/gdm/themes/Leon/leon-sesion.jpg
%{_datadir}/gdm/themes/Leon/leon-sistema.jpg
%{_datadir}/gdm/themes/Leon/leon.xml
%{_datadir}/gdm/themes/Leon/screenshot.jpg

#
# Theme 21/73
#
%files Gentoo_Emergence
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Gentoo_Emergence/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Gentoo_Emergence/gentoo-emergence.png
%{_datadir}/gdm/themes/Gentoo_Emergence/gentoo-emergence.xml
%{_datadir}/gdm/themes/Gentoo_Emergence/language.png
%{_datadir}/gdm/themes/Gentoo_Emergence/options.png
%{_datadir}/gdm/themes/Gentoo_Emergence/quit.png
%{_datadir}/gdm/themes/Gentoo_Emergence/screenshot.png
%{_datadir}/gdm/themes/Gentoo_Emergence/session.png
%{_datadir}/gdm/themes/Gentoo_Emergence/system.png

#
# Theme 22/73
#
%files FreeBSD_The_Power_of_Serve
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/FreeBSD.png
%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/FreeBSD.xml
%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/language.png
%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/options.png
%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/quit.png
%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/screenshot.png
%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/session.png
%{_datadir}/gdm/themes/FreeBSD_The_Power_of_Serve/system.png

#
# Theme 23/73
#
%files Daybreak
%defattr(644,root,root,755)
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
# Theme 24/73
#
%files Bijou
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Bijou/background.png
%{_datadir}/gdm/themes/Bijou/bijou.xml
%{_datadir}/gdm/themes/Bijou/disconnect.png
%{_datadir}/gdm/themes/Bijou/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Bijou/language.png
%{_datadir}/gdm/themes/Bijou/screenshot.png
%{_datadir}/gdm/themes/Bijou/session.png
%{_datadir}/gdm/themes/Bijou/system.png

#
# Theme 25/73
#
%files Stop_TCPA
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Stop_TCPA/background.jpg
%{_datadir}/gdm/themes/Stop_TCPA/disconnect.png
%{_datadir}/gdm/themes/Stop_TCPA/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Stop_TCPA/option.png
%{_datadir}/gdm/themes/Stop_TCPA/session.png
%{_datadir}/gdm/themes/Stop_TCPA/system.png
%{_datadir}/gdm/themes/Stop_TCPA/tcpa.xml

#
# Theme 26/73
#
%files Open_Source_Initiative
%defattr(644,root,root,755)
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
# Theme 27/73
#
%files FreeBSDarth
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/FreeBSDarth/FreeBSDarth.png
%{_datadir}/gdm/themes/FreeBSDarth/FreeBSDarth.xml
%{_datadir}/gdm/themes/FreeBSDarth/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/FreeBSDarth/help.png
%{_datadir}/gdm/themes/FreeBSDarth/options.png
%{_datadir}/gdm/themes/FreeBSDarth/screenshot.png
%{_datadir}/gdm/themes/FreeBSDarth/system.png

#
# Theme 28/73
#
%files Penguin_Computing
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Penguin_Computing/background.jpg
%{_datadir}/gdm/themes/Penguin_Computing/disconnect.png
%{_datadir}/gdm/themes/Penguin_Computing/galikynes.jpg
%{_datadir}/gdm/themes/Penguin_Computing/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Penguin_Computing/option.png
%{_datadir}/gdm/themes/Penguin_Computing/penguin.xml
%{_datadir}/gdm/themes/Penguin_Computing/session.png
%{_datadir}/gdm/themes/Penguin_Computing/system.png

#
# Theme 29/73
#
%files Knoke
%defattr(644,root,root,755)
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
# Theme 30/73
#
%files The_Dark_Crystal
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/The_Dark_Crystal/background.png
%{_datadir}/gdm/themes/The_Dark_Crystal/darkcrystal.xml
%{_datadir}/gdm/themes/The_Dark_Crystal/disconnect.png
%{_datadir}/gdm/themes/The_Dark_Crystal/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/The_Dark_Crystal/language.png
%{_datadir}/gdm/themes/The_Dark_Crystal/session.png
%{_datadir}/gdm/themes/The_Dark_Crystal/system.png

#
# Theme 31/73
#
%files Gnome_Chile
%defattr(644,root,root,755)
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
# Theme 32/73
#
%files Glassy
%defattr(644,root,root,755)
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
# Theme 33/73
#
%files Machu_Picchu
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Machu_Picchu/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Machu_Picchu/Machu?Picchu.xml
%{_datadir}/gdm/themes/Machu_Picchu/MP-ledge-bg.png
%{_datadir}/gdm/themes/Machu_Picchu/MP-tall-options.png
%{_datadir}/gdm/themes/Machu_Picchu/MP-tall-quit.png
%{_datadir}/gdm/themes/Machu_Picchu/MP-tall-session.png
%{_datadir}/gdm/themes/Machu_Picchu/MP-tall-system.png
%{_datadir}/gdm/themes/Machu_Picchu/screenshot.png

#
# Theme 34/73
#
%files RightVision
%defattr(644,root,root,755)
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
# Theme 35/73
#
%files La_Bisbal_dEmpord_nevada
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/labisbal-desconectar.jpg
%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/labisbal.jpg
%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/labisbal-opcions.jpg
%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/labisbal-sessio.jpg
%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/labisbal-sistema.jpg
%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/labisbal.xml
%{_datadir}/gdm/themes/La_Bisbal_dEmpord_nevada/screenshot.jpg

#
# Theme 36/73
#
%files Falling_Angel
%defattr(644,root,root,755)
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
# Theme 37/73
#
%files Hantzley
%defattr(644,root,root,755)
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
# Theme 38/73
#
%files Mozi
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Mozi/disconnect.png
%{_datadir}/gdm/themes/Mozi/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Mozi/mozilla.jpg
%{_datadir}/gdm/themes/Mozi/option.png
%{_datadir}/gdm/themes/Mozi/screenshot.png
%{_datadir}/gdm/themes/Mozi/session.png
%{_datadir}/gdm/themes/Mozi/soho.xml
%{_datadir}/gdm/themes/Mozi/system.png

#
# Theme 39/73
#
%files Todmorden
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Todmorden/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Todmorden/help.png
%{_datadir}/gdm/themes/Todmorden/options.png
%{_datadir}/gdm/themes/Todmorden/screenshot.jpg
%{_datadir}/gdm/themes/Todmorden/todmorden.jpg
%{_datadir}/gdm/themes/Todmorden/todmorden.xml

#
# Theme 40/73
#
%files Hunter
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Hunter/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Hunter/help.png
%{_datadir}/gdm/themes/Hunter/hunter.png
%{_datadir}/gdm/themes/Hunter/hunter.xml
%{_datadir}/gdm/themes/Hunter/options.png
%{_datadir}/gdm/themes/Hunter/screenshot.png

#
# Theme 41/73
#
%files GDM-Mosaic
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/GDM-Mosaic/disconnect.png
%{_datadir}/gdm/themes/GDM-Mosaic/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/GDM-Mosaic/Mosaic.png
%{_datadir}/gdm/themes/GDM-Mosaic/Mosaic.xml
%{_datadir}/gdm/themes/GDM-Mosaic/option.png
%{_datadir}/gdm/themes/GDM-Mosaic/screenshot.jpg
%{_datadir}/gdm/themes/GDM-Mosaic/session.png
%{_datadir}/gdm/themes/GDM-Mosaic/system.png

#
# Theme 42/73
#
%files KDE_Crystal
%defattr(644,root,root,755)
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
# Theme 43/73
#
%files Crystal_Rose
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Crystal_Rose/crystal-rose.jpg
%{_datadir}/gdm/themes/Crystal_Rose/crystal-rose.png
%{_datadir}/gdm/themes/Crystal_Rose/crystal-rose-screenshot.png
%{_datadir}/gdm/themes/Crystal_Rose/crystal-rose.xml
%{_datadir}/gdm/themes/Crystal_Rose/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Crystal_Rose/options.png
%{_datadir}/gdm/themes/Crystal_Rose/crystal-rose.png

#
# Theme 44/73
#
%files Devils_Candy
%defattr(644,root,root,755)
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
# Theme 45/73
#
%files Synergy
%defattr(644,root,root,755)
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
# Theme 46/73
#
%files Cubic_Linux_and_Gnome
%defattr(644,root,root,755)
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
# Theme 47/73
#
%files Butterfly
%defattr(644,root,root,755)
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
# Theme 48/73
#
%files Mirrored
%defattr(644,root,root,755)
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
# Theme 49/73
#
%files Delicious
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Delicious/delicious.xml
%{_datadir}/gdm/themes/Delicious/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Delicious/head1.png
%{_datadir}/gdm/themes/Delicious/mampf.png
%{_datadir}/gdm/themes/Delicious/screenshot.jpg
%{_datadir}/gdm/themes/Delicious/screenshot-small.png
%{_datadir}/gdm/themes/Delicious/sys.png

#
# Theme 50/73
#
%files Blue_Slack_GDM
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Blue_Slack_GDM/blueslack.png
%{_datadir}/gdm/themes/Blue_Slack_GDM/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Blue_Slack_GDM/language.png
%{_datadir}/gdm/themes/Blue_Slack_GDM/options.png
%{_datadir}/gdm/themes/Blue_Slack_GDM/quit.png
%{_datadir}/gdm/themes/Blue_Slack_GDM/screenshot.png
%{_datadir}/gdm/themes/Blue_Slack_GDM/session.png
%{_datadir}/gdm/themes/Blue_Slack_GDM/slackblue.xml
%{_datadir}/gdm/themes/Blue_Slack_GDM/system.png

#
# Theme 51/73
#
%files Dreaming_Alien
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Dreaming_Alien/background.png
%{_datadir}/gdm/themes/Dreaming_Alien/disconnect.png
%{_datadir}/gdm/themes/Dreaming_Alien/dreaming-alien.xml
%{_datadir}/gdm/themes/Dreaming_Alien/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Dreaming_Alien/language.png
%{_datadir}/gdm/themes/Dreaming_Alien/screenshot.png
%{_datadir}/gdm/themes/Dreaming_Alien/session.png
%{_datadir}/gdm/themes/Dreaming_Alien/system.png

#
# Theme 52/73
#
%files gcr-ddlm
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/gcr-ddlm/gcr-ddlm.background.png
%{_datadir}/gdm/themes/gcr-ddlm/gcr-ddlm.background.screenshot.png
%{_datadir}/gdm/themes/gcr-ddlm/gcr-ddlm.xml
%{_datadir}/gdm/themes/gcr-ddlm/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/gcr-ddlm/language.png
%{_datadir}/gdm/themes/gcr-ddlm/quit.png
%{_datadir}/gdm/themes/gcr-ddlm/session.png
%{_datadir}/gdm/themes/gcr-ddlm/system.png

#
# Theme 53/73
#
%files Gentoo_Cow
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Gentoo_Cow/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Gentoo_Cow/gentoo-cow-alpha.png
%{_datadir}/gdm/themes/Gentoo_Cow/gentoo-cow.xml
%{_datadir}/gdm/themes/Gentoo_Cow/options.png
%{_datadir}/gdm/themes/Gentoo_Cow/screenshot.jpg

#
# Theme 54/73
#
%files Just_BSD
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Just_BSD/BSD.png
%{_datadir}/gdm/themes/Just_BSD/BSD.xml
%{_datadir}/gdm/themes/Just_BSD/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Just_BSD/icon.png
%{_datadir}/gdm/themes/Just_BSD/options.png
%{_datadir}/gdm/themes/Just_BSD/quit.png

#
# Theme 55/73
#
%files pixelGDM
%defattr(644,root,root,755)
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
# Theme 56/73
#
%files Red_Leaves
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Red_Leaves/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Red_Leaves/leaves.png
%{_datadir}/gdm/themes/Red_Leaves/leaves-screenshot.png
%{_datadir}/gdm/themes/Red_Leaves/leaves.xml
%{_datadir}/gdm/themes/Red_Leaves/options.png

#
# Theme 57/73
#
%files Mono_Metal
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Mono_Metal/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Mono_Metal/language.png
%{_datadir}/gdm/themes/Mono_Metal/metal.png
%{_datadir}/gdm/themes/Mono_Metal/mono_metal.xml
%{_datadir}/gdm/themes/Mono_Metal/quit.png
%{_datadir}/gdm/themes/Mono_Metal/screenshot.png
%{_datadir}/gdm/themes/Mono_Metal/session.png
%{_datadir}/gdm/themes/Mono_Metal/system.png

#
# Theme 58/73
#
%files Gdm_Dropline
%defattr(644,root,root,755)
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
# Theme 59/73
#
%files Bee_at_Work
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Bee_at_Work/background.jpg
%{_datadir}/gdm/themes/Bee_at_Work/BeeAtWork.jpg
%{_datadir}/gdm/themes/Bee_at_Work/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Bee_at_Work/help.png
%{_datadir}/gdm/themes/Bee_at_Work/options.png
%{_datadir}/gdm/themes/Bee_at_Work/theme.xml

#
# Theme 60/73
#
%files LinuxTux
%defattr(644,root,root,755)
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
# Theme 61/73
#
%files Taipei
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Taipei/background.jpg
%{_datadir}/gdm/themes/Taipei/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Taipei/help.png
%{_datadir}/gdm/themes/Taipei/options.png
%{_datadir}/gdm/themes/Taipei/Taipei.jpg
%{_datadir}/gdm/themes/Taipei/theme.xml

#
# Theme 62/73
#
%files Odysseus
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Odysseus/background.jpg
%{_datadir}/gdm/themes/Odysseus/disconnect.png
%{_datadir}/gdm/themes/Odysseus/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Odysseus/Odysseus.xml
%{_datadir}/gdm/themes/Odysseus/option.png
%{_datadir}/gdm/themes/Odysseus/screenshot.png
%{_datadir}/gdm/themes/Odysseus/session.png
%{_datadir}/gdm/themes/Odysseus/system.png

#
# Theme 63/73
#
%files Kinkakuji
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Kinkakuji/background.jpg
%{_datadir}/gdm/themes/Kinkakuji/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Kinkakuji/help.png
%{_datadir}/gdm/themes/Kinkakuji/options.png
%{_datadir}/gdm/themes/Kinkakuji/screenshot.jpg
%{_datadir}/gdm/themes/Kinkakuji/theme.xml

#
# Theme 64/73
#
%files Milk
%defattr(644,root,root,755)
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
# Theme 65/73
#
%files Crop_Circles
%defattr(644,root,root,755)
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
# Theme 66/73
#
%files Angel
%defattr(644,root,root,755)
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
# Theme 67/73
#
%files Blueish
%defattr(644,root,root,755)
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
# Theme 68/73
#
%files Cracked_Windows
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Cracked_Windows/cracked-windows.jpg
%{_datadir}/gdm/themes/Cracked_Windows/cracked-windows.xml
%{_datadir}/gdm/themes/Cracked_Windows/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Cracked_Windows/language.png
%{_datadir}/gdm/themes/Cracked_Windows/quit.png
%{_datadir}/gdm/themes/Cracked_Windows/screenshot.jpg
%{_datadir}/gdm/themes/Cracked_Windows/session.png
%{_datadir}/gdm/themes/Cracked_Windows/system.png

#
# Theme 69/73
#
%files Crystal
%defattr(644,root,root,755)
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
# Theme 70/73
#
%files Dart_Frog
%defattr(644,root,root,755)
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
# Theme 71/73
#
%files DumbCloud
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/DumbCloud/cloud2.png
%{_datadir}/gdm/themes/DumbCloud/dumbcloud.svg
%{_datadir}/gdm/themes/DumbCloud/dumbcloud.xml
%{_datadir}/gdm/themes/DumbCloud/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/DumbCloud/help.png
%{_datadir}/gdm/themes/DumbCloud/options.png
%{_datadir}/gdm/themes/DumbCloud/test2.svg

#
# Theme 72/73
#
%files Emo-Blue
%defattr(644,root,root,755)
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
# Theme 73/73
#
%files Flowers
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Flowers/background.jpg
%{_datadir}/gdm/themes/Flowers/flowers.xml
%{_datadir}/gdm/themes/Flowers/GdmGreeterTheme.desktop
%{_datadir}/gdm/themes/Flowers/help.png
%{_datadir}/gdm/themes/Flowers/options.png
%{_datadir}/gdm/themes/Flowers/screenshot.jpg
%{_datadir}/gdm/themes/Flowers/system.png

%clean
rm -rf $RPM_BUILD_ROOT
