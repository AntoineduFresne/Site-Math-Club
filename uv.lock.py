version = 1
requires-python = ">=3.11"

[[package]]
name = "blinker"
version = "1.9.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/21/28/9b3f50ce0e048515135495f198351908d99540d69bfdc8c1d15b73dc55ce/blinker-1.9.0.tar.gz", hash = "sha256:b4ce2265a7abece45e7cc896e98dbebe6cead56bcf805a3d23136d145f5445bf", size = 22460 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/10/cb/f2ad4230dc2eb1a74edf38f1a38b9b52277f75bef262d8908e60d957e13c/blinker-1.9.0-py3-none-any.whl", hash = "sha256:ba0efaa9080b619ff2f3459d1d500c57bddea4a6b424b60a91141db6fd2f08bc", size = 8458 },
]

[[package]]
name = "click"
version = "8.1.8"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b9/2e/0090cbf739cee7d23781ad4b89a9894a41538e4fcf4c31dcdd705b78eb8b/click-8.1.8.tar.gz", hash = "sha256:ed53c9d8990d83c2a27deae68e4ee337473f6330c040a31d4225c9574d16096a", size = 226593 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7e/d4/7ebdbd03970677812aac39c869717059dbb71a4cfc033ca6e5221787892c/click-8.1.8-py3-none-any.whl", hash = "sha256:63c132bbbed01578a06712a2d1f497bb62d9c1c0d329b7903a866228027263b2", size = 98188 },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335 },
]

[[package]]
name = "dnspython"
version = "2.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b5/4a/263763cb2ba3816dd94b08ad3a33d5fdae34ecb856678773cc40a3605829/dnspython-2.7.0.tar.gz", hash = "sha256:ce9c432eda0dc91cf618a5cedf1a4e142651196bbcd2c80e89ed5a907e5cfaf1", size = 345197 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/68/1b/e0a87d256e40e8c888847551b20a017a6b98139178505dc7ffb96f04e954/dnspython-2.7.0-py3-none-any.whl", hash = "sha256:b4c34b7d10b51bcc3a5071e7b8dee77939f1e878477eeecc965e9835f63c6c86", size = 313632 },
]

[[package]]
name = "email-validator"
version = "2.2.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "dnspython" },
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/48/ce/13508a1ec3f8bb981ae4ca79ea40384becc868bfae97fd1c942bb3a001b1/email_validator-2.2.0.tar.gz", hash = "sha256:cb690f344c617a714f22e66ae771445a1ceb46821152df8e165c5f9a364582b7", size = 48967 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d7/ee/bf0adb559ad3c786f12bcbc9296b3f5675f529199bef03e2df281fa1fadb/email_validator-2.2.0-py3-none-any.whl", hash = "sha256:561977c2d73ce3611850a06fa56b414621e0c8faa9d66f2611407d87465da631", size = 33521 },
]

[[package]]
name = "flask"
version = "3.1.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "blinker" },
    { name = "click" },
    { name = "itsdangerous" },
    { name = "jinja2" },
    { name = "werkzeug" },
]
sdist = { url = "https://files.pythonhosted.org/packages/89/50/dff6380f1c7f84135484e176e0cac8690af72fa90e932ad2a0a60e28c69b/flask-3.1.0.tar.gz", hash = "sha256:5f873c5184c897c8d9d1b05df1e3d01b14910ce69607a117bd3277098a5836ac", size = 680824 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/af/47/93213ee66ef8fae3b93b3e29206f6b251e65c97bd91d8e1c5596ef15af0a/flask-3.1.0-py3-none-any.whl", hash = "sha256:d667207822eb83f1c4b50949b1623c8fc8d51f2341d65f72e1a1815397551136", size = 102979 },
]

[[package]]
name = "flask-login"
version = "0.6.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "flask" },
    { name = "werkzeug" },
]
sdist = { url = "https://files.pythonhosted.org/packages/c3/6e/2f4e13e373bb49e68c02c51ceadd22d172715a06716f9299d9df01b6ddb2/Flask-Login-0.6.3.tar.gz", hash = "sha256:5e23d14a607ef12806c699590b89d0f0e0d67baeec599d75947bf9c147330333", size = 48834 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/59/f5/67e9cc5c2036f58115f9fe0f00d203cf6780c3ff8ae0e705e7a9d9e8ff9e/Flask_Login-0.6.3-py3-none-any.whl", hash = "sha256:849b25b82a436bf830a054e74214074af59097171562ab10bfa999e6b78aae5d", size = 17303 },
]

[[package]]
name = "flask-sqlalchemy"
version = "3.1.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "flask" },
    { name = "sqlalchemy" },
]
sdist = { url = "https://files.pythonhosted.org/packages/91/53/b0a9fcc1b1297f51e68b69ed3b7c3c40d8c45be1391d77ae198712914392/flask_sqlalchemy-3.1.1.tar.gz", hash = "sha256:e4b68bb881802dda1a7d878b2fc84c06d1ee57fb40b874d3dc97dabfa36b8312", size = 81899 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1d/6a/89963a5c6ecf166e8be29e0d1bf6806051ee8fe6c82e232842e3aeac9204/flask_sqlalchemy-3.1.1-py3-none-any.whl", hash = "sha256:4ba4be7f419dc72f4efd8802d69974803c37259dd42f3913b0dcf75c9447e0a0", size = 25125 },
]

[[package]]
name = "flask-wtf"
version = "1.2.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "flask" },
    { name = "itsdangerous" },
    { name = "wtforms" },
]
sdist = { url = "https://files.pythonhosted.org/packages/80/9b/f1cd6e41bbf874f3436368f2c7ee3216c1e82d666ff90d1d800e20eb1317/flask_wtf-1.2.2.tar.gz", hash = "sha256:79d2ee1e436cf570bccb7d916533fa18757a2f18c290accffab1b9a0b684666b", size = 42641 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/dc/19/354449145fbebb65e7c621235b6ad69bebcfaec2142481f044d0ddc5b5c5/flask_wtf-1.2.2-py3-none-any.whl", hash = "sha256:e93160c5c5b6b571cf99300b6e01b72f9a101027cab1579901f8b10c5daf0b70", size = 12779 },
]

[[package]]
name = "greenlet"
version = "3.1.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/2f/ff/df5fede753cc10f6a5be0931204ea30c35fa2f2ea7a35b25bdaf4fe40e46/greenlet-3.1.1.tar.gz", hash = "sha256:4ce3ac6cdb6adf7946475d7ef31777c26d94bccc377e070a7986bd2d5c515467", size = 186022 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/28/62/1c2665558618553c42922ed47a4e6d6527e2fa3516a8256c2f431c5d0441/greenlet-3.1.1-cp311-cp311-macosx_11_0_universal2.whl", hash = "sha256:e4d333e558953648ca09d64f13e6d8f0523fa705f51cae3f03b5983489958c70", size = 272479 },
    { url = "https://files.pythonhosted.org/packages/76/9d/421e2d5f07285b6e4e3a676b016ca781f63cfe4a0cd8eaecf3fd6f7a71ae/greenlet-3.1.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:09fc016b73c94e98e29af67ab7b9a879c307c6731a2c9da0db5a7d9b7edd1159", size = 640404 },
    { url = "https://files.pythonhosted.org/packages/e5/de/6e05f5c59262a584e502dd3d261bbdd2c97ab5416cc9c0b91ea38932a901/greenlet-3.1.1-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:d5e975ca70269d66d17dd995dafc06f1b06e8cb1ec1e9ed54c1d1e4a7c4cf26e", size = 652813 },
    { url = "https://files.pythonhosted.org/packages/49/93/d5f93c84241acdea15a8fd329362c2c71c79e1a507c3f142a5d67ea435ae/greenlet-3.1.1-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:3b2813dc3de8c1ee3f924e4d4227999285fd335d1bcc0d2be6dc3f1f6a318ec1", size = 648517 },
    { url = "https://files.pythonhosted.org/packages/15/85/72f77fc02d00470c86a5c982b8daafdf65d38aefbbe441cebff3bf7037fc/greenlet-3.1.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e347b3bfcf985a05e8c0b7d462ba6f15b1ee1c909e2dcad795e49e91b152c383", size = 647831 },
    { url = "https://files.pythonhosted.org/packages/f7/4b/1c9695aa24f808e156c8f4813f685d975ca73c000c2a5056c514c64980f6/greenlet-3.1.1-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9e8f8c9cb53cdac7ba9793c276acd90168f416b9ce36799b9b885790f8ad6c0a", size = 602413 },
    { url = "https://files.pythonhosted.org/packages/76/70/ad6e5b31ef330f03b12559d19fda2606a522d3849cde46b24f223d6d1619/greenlet-3.1.1-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:62ee94988d6b4722ce0028644418d93a52429e977d742ca2ccbe1c4f4a792511", size = 1129619 },
    { url = "https://files.pythonhosted.org/packages/f4/fb/201e1b932e584066e0f0658b538e73c459b34d44b4bd4034f682423bc801/greenlet-3.1.1-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:1776fd7f989fc6b8d8c8cb8da1f6b82c5814957264d1f6cf818d475ec2bf6395", size = 1155198 },
    { url = "https://files.pythonhosted.org/packages/12/da/b9ed5e310bb8b89661b80cbcd4db5a067903bbcd7fc854923f5ebb4144f0/greenlet-3.1.1-cp311-cp311-win_amd64.whl", hash = "sha256:48ca08c771c268a768087b408658e216133aecd835c0ded47ce955381105ba39", size = 298930 },
    { url = "https://files.pythonhosted.org/packages/7d/ec/bad1ac26764d26aa1353216fcbfa4670050f66d445448aafa227f8b16e80/greenlet-3.1.1-cp312-cp312-macosx_11_0_universal2.whl", hash = "sha256:4afe7ea89de619adc868e087b4d2359282058479d7cfb94970adf4b55284574d", size = 274260 },
    { url = "https://files.pythonhosted.org/packages/66/d4/c8c04958870f482459ab5956c2942c4ec35cac7fe245527f1039837c17a9/greenlet-3.1.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f406b22b7c9a9b4f8aa9d2ab13d6ae0ac3e85c9a809bd590ad53fed2bf70dc79", size = 649064 },
    { url = "https://files.pythonhosted.org/packages/51/41/467b12a8c7c1303d20abcca145db2be4e6cd50a951fa30af48b6ec607581/greenlet-3.1.1-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:c3a701fe5a9695b238503ce5bbe8218e03c3bcccf7e204e455e7462d770268aa", size = 663420 },
    { url = "https://files.pythonhosted.org/packages/27/8f/2a93cd9b1e7107d5c7b3b7816eeadcac2ebcaf6d6513df9abaf0334777f6/greenlet-3.1.1-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2846930c65b47d70b9d178e89c7e1a69c95c1f68ea5aa0a58646b7a96df12441", size = 658035 },
    { url = "https://files.pythonhosted.org/packages/57/5c/7c6f50cb12be092e1dccb2599be5a942c3416dbcfb76efcf54b3f8be4d8d/greenlet-3.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:99cfaa2110534e2cf3ba31a7abcac9d328d1d9f1b95beede58294a60348fba36", size = 660105 },
    { url = "https://files.pythonhosted.org/packages/f1/66/033e58a50fd9ec9df00a8671c74f1f3a320564c6415a4ed82a1c651654ba/greenlet-3.1.1-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1443279c19fca463fc33e65ef2a935a5b09bb90f978beab37729e1c3c6c25fe9", size = 613077 },
    { url = "https://files.pythonhosted.org/packages/19/c5/36384a06f748044d06bdd8776e231fadf92fc896bd12cb1c9f5a1bda9578/greenlet-3.1.1-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:b7cede291382a78f7bb5f04a529cb18e068dd29e0fb27376074b6d0317bf4dd0", size = 1135975 },
    { url = "https://files.pythonhosted.org/packages/38/f9/c0a0eb61bdf808d23266ecf1d63309f0e1471f284300ce6dac0ae1231881/greenlet-3.1.1-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:23f20bb60ae298d7d8656c6ec6db134bca379ecefadb0b19ce6f19d1f232a942", size = 1163955 },
    { url = "https://files.pythonhosted.org/packages/43/21/a5d9df1d21514883333fc86584c07c2b49ba7c602e670b174bd73cfc9c7f/greenlet-3.1.1-cp312-cp312-win_amd64.whl", hash = "sha256:7124e16b4c55d417577c2077be379514321916d5790fa287c9ed6f23bd2ffd01", size = 299655 },
    { url = "https://files.pythonhosted.org/packages/f3/57/0db4940cd7bb461365ca8d6fd53e68254c9dbbcc2b452e69d0d41f10a85e/greenlet-3.1.1-cp313-cp313-macosx_11_0_universal2.whl", hash = "sha256:05175c27cb459dcfc05d026c4232f9de8913ed006d42713cb8a5137bd49375f1", size = 272990 },
    { url = "https://files.pythonhosted.org/packages/1c/ec/423d113c9f74e5e402e175b157203e9102feeb7088cee844d735b28ef963/greenlet-3.1.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:935e943ec47c4afab8965954bf49bfa639c05d4ccf9ef6e924188f762145c0ff", size = 649175 },
    { url = "https://files.pythonhosted.org/packages/a9/46/ddbd2db9ff209186b7b7c621d1432e2f21714adc988703dbdd0e65155c77/greenlet-3.1.1-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:667a9706c970cb552ede35aee17339a18e8f2a87a51fba2ed39ceeeb1004798a", size = 663425 },
    { url = "https://files.pythonhosted.org/packages/bc/f9/9c82d6b2b04aa37e38e74f0c429aece5eeb02bab6e3b98e7db89b23d94c6/greenlet-3.1.1-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:b8a678974d1f3aa55f6cc34dc480169d58f2e6d8958895d68845fa4ab566509e", size = 657736 },
    { url = "https://files.pythonhosted.org/packages/d9/42/b87bc2a81e3a62c3de2b0d550bf91a86939442b7ff85abb94eec3fc0e6aa/greenlet-3.1.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:efc0f674aa41b92da8c49e0346318c6075d734994c3c4e4430b1c3f853e498e4", size = 660347 },
    { url = "https://files.pythonhosted.org/packages/37/fa/71599c3fd06336cdc3eac52e6871cfebab4d9d70674a9a9e7a482c318e99/greenlet-3.1.1-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0153404a4bb921f0ff1abeb5ce8a5131da56b953eda6e14b88dc6bbc04d2049e", size = 615583 },
    { url = "https://files.pythonhosted.org/packages/4e/96/e9ef85de031703ee7a4483489b40cf307f93c1824a02e903106f2ea315fe/greenlet-3.1.1-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:275f72decf9932639c1c6dd1013a1bc266438eb32710016a1c742df5da6e60a1", size = 1133039 },
    { url = "https://files.pythonhosted.org/packages/87/76/b2b6362accd69f2d1889db61a18c94bc743e961e3cab344c2effaa4b4a25/greenlet-3.1.1-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:c4aab7f6381f38a4b42f269057aee279ab0fc7bf2e929e3d4abfae97b682a12c", size = 1160716 },
    { url = "https://files.pythonhosted.org/packages/1f/1b/54336d876186920e185066d8c3024ad55f21d7cc3683c856127ddb7b13ce/greenlet-3.1.1-cp313-cp313-win_amd64.whl", hash = "sha256:b42703b1cf69f2aa1df7d1030b9d77d3e584a70755674d60e710f0af570f3761", size = 299490 },
    { url = "https://files.pythonhosted.org/packages/5f/17/bea55bf36990e1638a2af5ba10c1640273ef20f627962cf97107f1e5d637/greenlet-3.1.1-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f1695e76146579f8c06c1509c7ce4dfe0706f49c6831a817ac04eebb2fd02011", size = 643731 },
    { url = "https://files.pythonhosted.org/packages/78/d2/aa3d2157f9ab742a08e0fd8f77d4699f37c22adfbfeb0c610a186b5f75e0/greenlet-3.1.1-cp313-cp313t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:7876452af029456b3f3549b696bb36a06db7c90747740c5302f74a9e9fa14b13", size = 649304 },
    { url = "https://files.pythonhosted.org/packages/f1/8e/d0aeffe69e53ccff5a28fa86f07ad1d2d2d6537a9506229431a2a02e2f15/greenlet-3.1.1-cp313-cp313t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:4ead44c85f8ab905852d3de8d86f6f8baf77109f9da589cb4fa142bd3b57b475", size = 646537 },
    { url = "https://files.pythonhosted.org/packages/05/79/e15408220bbb989469c8871062c97c6c9136770657ba779711b90870d867/greenlet-3.1.1-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8320f64b777d00dd7ccdade271eaf0cad6636343293a25074cc5566160e4de7b", size = 642506 },
    { url = "https://files.pythonhosted.org/packages/18/87/470e01a940307796f1d25f8167b551a968540fbe0551c0ebb853cb527dd6/greenlet-3.1.1-cp313-cp313t-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:6510bf84a6b643dabba74d3049ead221257603a253d0a9873f55f6a59a65f822", size = 602753 },
    { url = "https://files.pythonhosted.org/packages/e2/72/576815ba674eddc3c25028238f74d7b8068902b3968cbe456771b166455e/greenlet-3.1.1-cp313-cp313t-musllinux_1_1_aarch64.whl", hash = "sha256:04b013dc07c96f83134b1e99888e7a79979f1a247e2a9f59697fa14b5862ed01", size = 1122731 },
    { url = "https://files.pythonhosted.org/packages/ac/38/08cc303ddddc4b3d7c628c3039a61a3aae36c241ed01393d00c2fd663473/greenlet-3.1.1-cp313-cp313t-musllinux_1_1_x86_64.whl", hash = "sha256:411f015496fec93c1c8cd4e5238da364e1da7a124bcb293f085bf2860c32c6f6", size = 1142112 },
]

[[package]]
name = "gunicorn"
version = "23.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "packaging" },
]
sdist = { url = "https://files.pythonhosted.org/packages/34/72/9614c465dc206155d93eff0ca20d42e1e35afc533971379482de953521a4/gunicorn-23.0.0.tar.gz", hash = "sha256:f014447a0101dc57e294f6c18ca6b40227a4c90e9bdb586042628030cba004ec", size = 375031 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/cb/7d/6dac2a6e1eba33ee43f318edbed4ff29151a49b5d37f080aad1e6469bca4/gunicorn-23.0.0-py3-none-any.whl", hash = "sha256:ec400d38950de4dfd418cff8328b2c8faed0edb0d517d3394e457c317908ca4d", size = 85029 },
]

[[package]]
name = "idna"
version = "3.10"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f1/70/7703c29685631f5a7590aa73f1f1d3fa9a380e654b86af429e0934a32f7d/idna-3.10.tar.gz", hash = "sha256:12f65c9b470abda6dc35cf8e63cc574b1c52b11df2c86030af0ac09b01b13ea9", size = 190490 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/76/c6/c88e154df9c4e1a2a66ccf0005a88dfb2650c1dffb6f5ce603dfbd452ce3/idna-3.10-py3-none-any.whl", hash = "sha256:946d195a0d259cbba61165e88e65941f16e9b36ea6ddb97f00452bae8b1287d3", size = 70442 },
]

[[package]]
name = "itsdangerous"
version = "2.2.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/9c/cb/8ac0172223afbccb63986cc25049b154ecfb5e85932587206f42317be31d/itsdangerous-2.2.0.tar.gz", hash = "sha256:e0050c0b7da1eea53ffaf149c0cfbb5c6e2e2b69c4bef22c81fa6eb73e5f6173", size = 54410 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/96/92447566d16df59b2a776c0fb82dbc4d9e07cd95062562af01e408583fc4/itsdangerous-2.2.0-py3-none-any.whl", hash = "sha256:c6242fc49e35958c8b15141343aa660db5fc54d4f13a1db01a3f5891b98700ef", size = 16234 },
]

[[package]]
name = "jinja2"
version = "3.1.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markupsafe" },
]
sdist = { url = "https://files.pythonhosted.org/packages/af/92/b3130cbbf5591acf9ade8708c365f3238046ac7cb8ccba6e81abccb0ccff/jinja2-3.1.5.tar.gz", hash = "sha256:8fefff8dc3034e27bb80d67c671eb8a9bc424c0ef4c0826edbff304cceff43bb", size = 244674 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/bd/0f/2ba5fbcd631e3e88689309dbe978c5769e883e4b84ebfe7da30b43275c5a/jinja2-3.1.5-py3-none-any.whl", hash = "sha256:aba0f4dc9ed8013c424088f68a5c226f7d6097ed89b246d7749c2ec4175c6adb", size = 134596 },
]

[[package]]
name = "markupsafe"
version = "3.0.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b2/97/5d42485e71dfc078108a86d6de8fa46db44a1a9295e89c5d6d4a06e23a62/markupsafe-3.0.2.tar.gz", hash = "sha256:ee55d3edf80167e48ea11a923c7386f4669df67d7994554387f84e7d8b0a2bf0", size = 20537 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/6b/28/bbf83e3f76936960b850435576dd5e67034e200469571be53f69174a2dfd/MarkupSafe-3.0.2-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:9025b4018f3a1314059769c7bf15441064b2207cb3f065e6ea1e7359cb46db9d", size = 14353 },
    { url = "https://files.pythonhosted.org/packages/6c/30/316d194b093cde57d448a4c3209f22e3046c5bb2fb0820b118292b334be7/MarkupSafe-3.0.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:93335ca3812df2f366e80509ae119189886b0f3c2b81325d39efdb84a1e2ae93", size = 12392 },
    { url = "https://files.pythonhosted.org/packages/f2/96/9cdafba8445d3a53cae530aaf83c38ec64c4d5427d975c974084af5bc5d2/MarkupSafe-3.0.2-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:2cb8438c3cbb25e220c2ab33bb226559e7afb3baec11c4f218ffa7308603c832", size = 23984 },
    { url = "https://files.pythonhosted.org/packages/f1/a4/aefb044a2cd8d7334c8a47d3fb2c9f328ac48cb349468cc31c20b539305f/MarkupSafe-3.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:a123e330ef0853c6e822384873bef7507557d8e4a082961e1defa947aa59ba84", size = 23120 },
    { url = "https://files.pythonhosted.org/packages/8d/21/5e4851379f88f3fad1de30361db501300d4f07bcad047d3cb0449fc51f8c/MarkupSafe-3.0.2-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:1e084f686b92e5b83186b07e8a17fc09e38fff551f3602b249881fec658d3eca", size = 23032 },
    { url = "https://files.pythonhosted.org/packages/00/7b/e92c64e079b2d0d7ddf69899c98842f3f9a60a1ae72657c89ce2655c999d/MarkupSafe-3.0.2-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:d8213e09c917a951de9d09ecee036d5c7d36cb6cb7dbaece4c71a60d79fb9798", size = 24057 },
    { url = "https://files.pythonhosted.org/packages/f9/ac/46f960ca323037caa0a10662ef97d0a4728e890334fc156b9f9e52bcc4ca/MarkupSafe-3.0.2-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:5b02fb34468b6aaa40dfc198d813a641e3a63b98c2b05a16b9f80b7ec314185e", size = 23359 },
    { url = "https://files.pythonhosted.org/packages/69/84/83439e16197337b8b14b6a5b9c2105fff81d42c2a7c5b58ac7b62ee2c3b1/MarkupSafe-3.0.2-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:0bff5e0ae4ef2e1ae4fdf2dfd5b76c75e5c2fa4132d05fc1b0dabcd20c7e28c4", size = 23306 },
    { url = "https://files.pythonhosted.org/packages/9a/34/a15aa69f01e2181ed8d2b685c0d2f6655d5cca2c4db0ddea775e631918cd/MarkupSafe-3.0.2-cp311-cp311-win32.whl", hash = "sha256:6c89876f41da747c8d3677a2b540fb32ef5715f97b66eeb0c6b66f5e3ef6f59d", size = 15094 },
    { url = "https://files.pythonhosted.org/packages/da/b8/3a3bd761922d416f3dc5d00bfbed11f66b1ab89a0c2b6e887240a30b0f6b/MarkupSafe-3.0.2-cp311-cp311-win_amd64.whl", hash = "sha256:70a87b411535ccad5ef2f1df5136506a10775d267e197e4cf531ced10537bd6b", size = 15521 },
    { url = "https://files.pythonhosted.org/packages/22/09/d1f21434c97fc42f09d290cbb6350d44eb12f09cc62c9476effdb33a18aa/MarkupSafe-3.0.2-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:9778bd8ab0a994ebf6f84c2b949e65736d5575320a17ae8984a77fab08db94cf", size = 14274 },
    { url = "https://files.pythonhosted.org/packages/6b/b0/18f76bba336fa5aecf79d45dcd6c806c280ec44538b3c13671d49099fdd0/MarkupSafe-3.0.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:846ade7b71e3536c4e56b386c2a47adf5741d2d8b94ec9dc3e92e5e1ee1e2225", size = 12348 },
    { url = "https://files.pythonhosted.org/packages/e0/25/dd5c0f6ac1311e9b40f4af06c78efde0f3b5cbf02502f8ef9501294c425b/MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1c99d261bd2d5f6b59325c92c73df481e05e57f19837bdca8413b9eac4bd8028", size = 24149 },
    { url = "https://files.pythonhosted.org/packages/f3/f0/89e7aadfb3749d0f52234a0c8c7867877876e0a20b60e2188e9850794c17/MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e17c96c14e19278594aa4841ec148115f9c7615a47382ecb6b82bd8fea3ab0c8", size = 23118 },
    { url = "https://files.pythonhosted.org/packages/d5/da/f2eeb64c723f5e3777bc081da884b414671982008c47dcc1873d81f625b6/MarkupSafe-3.0.2-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:88416bd1e65dcea10bc7569faacb2c20ce071dd1f87539ca2ab364bf6231393c", size = 22993 },
    { url = "https://files.pythonhosted.org/packages/da/0e/1f32af846df486dce7c227fe0f2398dc7e2e51d4a370508281f3c1c5cddc/MarkupSafe-3.0.2-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:2181e67807fc2fa785d0592dc2d6206c019b9502410671cc905d132a92866557", size = 24178 },
    { url = "https://files.pythonhosted.org/packages/c4/f6/bb3ca0532de8086cbff5f06d137064c8410d10779c4c127e0e47d17c0b71/MarkupSafe-3.0.2-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:52305740fe773d09cffb16f8ed0427942901f00adedac82ec8b67752f58a1b22", size = 23319 },
    { url = "https://files.pythonhosted.org/packages/a2/82/8be4c96ffee03c5b4a034e60a31294daf481e12c7c43ab8e34a1453ee48b/MarkupSafe-3.0.2-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:ad10d3ded218f1039f11a75f8091880239651b52e9bb592ca27de44eed242a48", size = 23352 },
    { url = "https://files.pythonhosted.org/packages/51/ae/97827349d3fcffee7e184bdf7f41cd6b88d9919c80f0263ba7acd1bbcb18/MarkupSafe-3.0.2-cp312-cp312-win32.whl", hash = "sha256:0f4ca02bea9a23221c0182836703cbf8930c5e9454bacce27e767509fa286a30", size = 15097 },
    { url = "https://files.pythonhosted.org/packages/c1/80/a61f99dc3a936413c3ee4e1eecac96c0da5ed07ad56fd975f1a9da5bc630/MarkupSafe-3.0.2-cp312-cp312-win_amd64.whl", hash = "sha256:8e06879fc22a25ca47312fbe7c8264eb0b662f6db27cb2d3bbbc74b1df4b9b87", size = 15601 },
    { url = "https://files.pythonhosted.org/packages/83/0e/67eb10a7ecc77a0c2bbe2b0235765b98d164d81600746914bebada795e97/MarkupSafe-3.0.2-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:ba9527cdd4c926ed0760bc301f6728ef34d841f405abf9d4f959c478421e4efd", size = 14274 },
    { url = "https://files.pythonhosted.org/packages/2b/6d/9409f3684d3335375d04e5f05744dfe7e9f120062c9857df4ab490a1031a/MarkupSafe-3.0.2-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:f8b3d067f2e40fe93e1ccdd6b2e1d16c43140e76f02fb1319a05cf2b79d99430", size = 12352 },
    { url = "https://files.pythonhosted.org/packages/d2/f5/6eadfcd3885ea85fe2a7c128315cc1bb7241e1987443d78c8fe712d03091/MarkupSafe-3.0.2-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:569511d3b58c8791ab4c2e1285575265991e6d8f8700c7be0e88f86cb0672094", size = 24122 },
    { url = "https://files.pythonhosted.org/packages/0c/91/96cf928db8236f1bfab6ce15ad070dfdd02ed88261c2afafd4b43575e9e9/MarkupSafe-3.0.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:15ab75ef81add55874e7ab7055e9c397312385bd9ced94920f2802310c930396", size = 23085 },
    { url = "https://files.pythonhosted.org/packages/c2/cf/c9d56af24d56ea04daae7ac0940232d31d5a8354f2b457c6d856b2057d69/MarkupSafe-3.0.2-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:f3818cb119498c0678015754eba762e0d61e5b52d34c8b13d770f0719f7b1d79", size = 22978 },
    { url = "https://files.pythonhosted.org/packages/2a/9f/8619835cd6a711d6272d62abb78c033bda638fdc54c4e7f4272cf1c0962b/MarkupSafe-3.0.2-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:cdb82a876c47801bb54a690c5ae105a46b392ac6099881cdfb9f6e95e4014c6a", size = 24208 },
    { url = "https://files.pythonhosted.org/packages/f9/bf/176950a1792b2cd2102b8ffeb5133e1ed984547b75db47c25a67d3359f77/MarkupSafe-3.0.2-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:cabc348d87e913db6ab4aa100f01b08f481097838bdddf7c7a84b7575b7309ca", size = 23357 },
    { url = "https://files.pythonhosted.org/packages/ce/4f/9a02c1d335caabe5c4efb90e1b6e8ee944aa245c1aaaab8e8a618987d816/MarkupSafe-3.0.2-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:444dcda765c8a838eaae23112db52f1efaf750daddb2d9ca300bcae1039adc5c", size = 23344 },
    { url = "https://files.pythonhosted.org/packages/ee/55/c271b57db36f748f0e04a759ace9f8f759ccf22b4960c270c78a394f58be/MarkupSafe-3.0.2-cp313-cp313-win32.whl", hash = "sha256:bcf3e58998965654fdaff38e58584d8937aa3096ab5354d493c77d1fdd66d7a1", size = 15101 },
    { url = "https://files.pythonhosted.org/packages/29/88/07df22d2dd4df40aba9f3e402e6dc1b8ee86297dddbad4872bd5e7b0094f/MarkupSafe-3.0.2-cp313-cp313-win_amd64.whl", hash = "sha256:e6a2a455bd412959b57a172ce6328d2dd1f01cb2135efda2e4576e8a23fa3b0f", size = 15603 },
    { url = "https://files.pythonhosted.org/packages/62/6a/8b89d24db2d32d433dffcd6a8779159da109842434f1dd2f6e71f32f738c/MarkupSafe-3.0.2-cp313-cp313t-macosx_10_13_universal2.whl", hash = "sha256:b5a6b3ada725cea8a5e634536b1b01c30bcdcd7f9c6fff4151548d5bf6b3a36c", size = 14510 },
    { url = "https://files.pythonhosted.org/packages/7a/06/a10f955f70a2e5a9bf78d11a161029d278eeacbd35ef806c3fd17b13060d/MarkupSafe-3.0.2-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:a904af0a6162c73e3edcb969eeeb53a63ceeb5d8cf642fade7d39e7963a22ddb", size = 12486 },
    { url = "https://files.pythonhosted.org/packages/34/cf/65d4a571869a1a9078198ca28f39fba5fbb910f952f9dbc5220afff9f5e6/MarkupSafe-3.0.2-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:4aa4e5faecf353ed117801a068ebab7b7e09ffb6e1d5e412dc852e0da018126c", size = 25480 },
    { url = "https://files.pythonhosted.org/packages/0c/e3/90e9651924c430b885468b56b3d597cabf6d72be4b24a0acd1fa0e12af67/MarkupSafe-3.0.2-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c0ef13eaeee5b615fb07c9a7dadb38eac06a0608b41570d8ade51c56539e509d", size = 23914 },
    { url = "https://files.pythonhosted.org/packages/66/8c/6c7cf61f95d63bb866db39085150df1f2a5bd3335298f14a66b48e92659c/MarkupSafe-3.0.2-cp313-cp313t-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:d16a81a06776313e817c951135cf7340a3e91e8c1ff2fac444cfd75fffa04afe", size = 23796 },
    { url = "https://files.pythonhosted.org/packages/bb/35/cbe9238ec3f47ac9a7c8b3df7a808e7cb50fe149dc7039f5f454b3fba218/MarkupSafe-3.0.2-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:6381026f158fdb7c72a168278597a5e3a5222e83ea18f543112b2662a9b699c5", size = 25473 },
    { url = "https://files.pythonhosted.org/packages/e6/32/7621a4382488aa283cc05e8984a9c219abad3bca087be9ec77e89939ded9/MarkupSafe-3.0.2-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:3d79d162e7be8f996986c064d1c7c817f6df3a77fe3d6859f6f9e7be4b8c213a", size = 24114 },
    { url = "https://files.pythonhosted.org/packages/0d/80/0985960e4b89922cb5a0bac0ed39c5b96cbc1a536a99f30e8c220a996ed9/MarkupSafe-3.0.2-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:131a3c7689c85f5ad20f9f6fb1b866f402c445b220c19fe4308c0b147ccd2ad9", size = 24098 },
    { url = "https://files.pythonhosted.org/packages/82/78/fedb03c7d5380df2427038ec8d973587e90561b2d90cd472ce9254cf348b/MarkupSafe-3.0.2-cp313-cp313t-win32.whl", hash = "sha256:ba8062ed2cf21c07a9e295d5b8a2a5ce678b913b45fdf68c32d95d6c1291e0b6", size = 15208 },
    { url = "https://files.pythonhosted.org/packages/4f/65/6079a46068dfceaeabb5dcad6d674f5f5c61a6fa5673746f42a9f4c233b3/MarkupSafe-3.0.2-cp313-cp313t-win_amd64.whl", hash = "sha256:e444a31f8db13eb18ada366ab3cf45fd4b31e4db1236a4448f68778c1d1a5a2f", size = 15739 },
]

[[package]]
name = "packaging"
version = "24.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d0/63/68dbb6eb2de9cb10ee4c9c14a0148804425e13c4fb20d61cce69f53106da/packaging-24.2.tar.gz", hash = "sha256:c228a6dc5e932d346bc5739379109d49e8853dd8223571c7c5b55260edc0b97f", size = 163950 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/88/ef/eb23f262cca3c0c4eb7ab1933c3b1f03d021f2c48f54763065b6f0e321be/packaging-24.2-py3-none-any.whl", hash = "sha256:09abb1bccd265c01f4a3aa3f7a7db064b36514d2cba19a2f694fe6150451a759", size = 65451 },
]

[[package]]
name = "psycopg2-binary"
version = "2.9.10"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/cb/0e/bdc8274dc0585090b4e3432267d7be4dfbfd8971c0fa59167c711105a6bf/psycopg2-binary-2.9.10.tar.gz", hash = "sha256:4b3df0e6990aa98acda57d983942eff13d824135fe2250e6522edaa782a06de2", size = 385764 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9c/8f/9feb01291d0d7a0a4c6a6bab24094135c2b59c6a81943752f632c75896d6/psycopg2_binary-2.9.10-cp311-cp311-macosx_12_0_x86_64.whl", hash = "sha256:04392983d0bb89a8717772a193cfaac58871321e3ec69514e1c4e0d4957b5aff", size = 3043397 },
    { url = "https://files.pythonhosted.org/packages/15/30/346e4683532011561cd9c8dfeac6a8153dd96452fee0b12666058ab7893c/psycopg2_binary-2.9.10-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:1a6784f0ce3fec4edc64e985865c17778514325074adf5ad8f80636cd029ef7c", size = 3274806 },
    { url = "https://files.pythonhosted.org/packages/66/6e/4efebe76f76aee7ec99166b6c023ff8abdc4e183f7b70913d7c047701b79/psycopg2_binary-2.9.10-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b5f86c56eeb91dc3135b3fd8a95dc7ae14c538a2f3ad77a19645cf55bab1799c", size = 2851370 },
    { url = "https://files.pythonhosted.org/packages/7f/fd/ff83313f86b50f7ca089b161b8e0a22bb3c319974096093cd50680433fdb/psycopg2_binary-2.9.10-cp311-cp311-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:2b3d2491d4d78b6b14f76881905c7a8a8abcf974aad4a8a0b065273a0ed7a2cb", size = 3080780 },
    { url = "https://files.pythonhosted.org/packages/e6/c4/bfadd202dcda8333a7ccafdc51c541dbdfce7c2c7cda89fa2374455d795f/psycopg2_binary-2.9.10-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:2286791ececda3a723d1910441c793be44625d86d1a4e79942751197f4d30341", size = 3264583 },
    { url = "https://files.pythonhosted.org/packages/5d/f1/09f45ac25e704ac954862581f9f9ae21303cc5ded3d0b775532b407f0e90/psycopg2_binary-2.9.10-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:512d29bb12608891e349af6a0cccedce51677725a921c07dba6342beaf576f9a", size = 3019831 },
    { url = "https://files.pythonhosted.org/packages/9e/2e/9beaea078095cc558f215e38f647c7114987d9febfc25cb2beed7c3582a5/psycopg2_binary-2.9.10-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:5a507320c58903967ef7384355a4da7ff3f28132d679aeb23572753cbf2ec10b", size = 2871822 },
    { url = "https://files.pythonhosted.org/packages/01/9e/ef93c5d93f3dc9fc92786ffab39e323b9aed066ba59fdc34cf85e2722271/psycopg2_binary-2.9.10-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:6d4fa1079cab9018f4d0bd2db307beaa612b0d13ba73b5c6304b9fe2fb441ff7", size = 2820975 },
    { url = "https://files.pythonhosted.org/packages/a5/f0/049e9631e3268fe4c5a387f6fc27e267ebe199acf1bc1bc9cbde4bd6916c/psycopg2_binary-2.9.10-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:851485a42dbb0bdc1edcdabdb8557c09c9655dfa2ca0460ff210522e073e319e", size = 2919320 },
    { url = "https://files.pythonhosted.org/packages/dc/9a/bcb8773b88e45fb5a5ea8339e2104d82c863a3b8558fbb2aadfe66df86b3/psycopg2_binary-2.9.10-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:35958ec9e46432d9076286dda67942ed6d968b9c3a6a2fd62b48939d1d78bf68", size = 2957617 },
    { url = "https://files.pythonhosted.org/packages/e2/6b/144336a9bf08a67d217b3af3246abb1d027095dab726f0687f01f43e8c03/psycopg2_binary-2.9.10-cp311-cp311-win32.whl", hash = "sha256:ecced182e935529727401b24d76634a357c71c9275b356efafd8a2a91ec07392", size = 1024618 },
    { url = "https://files.pythonhosted.org/packages/61/69/3b3d7bd583c6d3cbe5100802efa5beacaacc86e37b653fc708bf3d6853b8/psycopg2_binary-2.9.10-cp311-cp311-win_amd64.whl", hash = "sha256:ee0e8c683a7ff25d23b55b11161c2663d4b099770f6085ff0a20d4505778d6b4", size = 1163816 },
    { url = "https://files.pythonhosted.org/packages/49/7d/465cc9795cf76f6d329efdafca74693714556ea3891813701ac1fee87545/psycopg2_binary-2.9.10-cp312-cp312-macosx_12_0_x86_64.whl", hash = "sha256:880845dfe1f85d9d5f7c412efea7a08946a46894537e4e5d091732eb1d34d9a0", size = 3044771 },
    { url = "https://files.pythonhosted.org/packages/8b/31/6d225b7b641a1a2148e3ed65e1aa74fc86ba3fee850545e27be9e1de893d/psycopg2_binary-2.9.10-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:9440fa522a79356aaa482aa4ba500b65f28e5d0e63b801abf6aa152a29bd842a", size = 3275336 },
    { url = "https://files.pythonhosted.org/packages/30/b7/a68c2b4bff1cbb1728e3ec864b2d92327c77ad52edcd27922535a8366f68/psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e3923c1d9870c49a2d44f795df0c889a22380d36ef92440ff618ec315757e539", size = 2851637 },
    { url = "https://files.pythonhosted.org/packages/0b/b1/cfedc0e0e6f9ad61f8657fd173b2f831ce261c02a08c0b09c652b127d813/psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:7b2c956c028ea5de47ff3a8d6b3cc3330ab45cf0b7c3da35a2d6ff8420896526", size = 3082097 },
    { url = "https://files.pythonhosted.org/packages/18/ed/0a8e4153c9b769f59c02fb5e7914f20f0b2483a19dae7bf2db54b743d0d0/psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f758ed67cab30b9a8d2833609513ce4d3bd027641673d4ebc9c067e4d208eec1", size = 3264776 },
    { url = "https://files.pythonhosted.org/packages/10/db/d09da68c6a0cdab41566b74e0a6068a425f077169bed0946559b7348ebe9/psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8cd9b4f2cfab88ed4a9106192de509464b75a906462fb846b936eabe45c2063e", size = 3020968 },
    { url = "https://files.pythonhosted.org/packages/94/28/4d6f8c255f0dfffb410db2b3f9ac5218d959a66c715c34cac31081e19b95/psycopg2_binary-2.9.10-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:6dc08420625b5a20b53551c50deae6e231e6371194fa0651dbe0fb206452ae1f", size = 2872334 },
    { url = "https://files.pythonhosted.org/packages/05/f7/20d7bf796593c4fea95e12119d6cc384ff1f6141a24fbb7df5a668d29d29/psycopg2_binary-2.9.10-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:d7cd730dfa7c36dbe8724426bf5612798734bff2d3c3857f36f2733f5bfc7c00", size = 2822722 },
    { url = "https://files.pythonhosted.org/packages/4d/e4/0c407ae919ef626dbdb32835a03b6737013c3cc7240169843965cada2bdf/psycopg2_binary-2.9.10-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:155e69561d54d02b3c3209545fb08938e27889ff5a10c19de8d23eb5a41be8a5", size = 2920132 },
    { url = "https://files.pythonhosted.org/packages/2d/70/aa69c9f69cf09a01da224909ff6ce8b68faeef476f00f7ec377e8f03be70/psycopg2_binary-2.9.10-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:c3cc28a6fd5a4a26224007712e79b81dbaee2ffb90ff406256158ec4d7b52b47", size = 2959312 },
    { url = "https://files.pythonhosted.org/packages/d3/bd/213e59854fafe87ba47814bf413ace0dcee33a89c8c8c814faca6bc7cf3c/psycopg2_binary-2.9.10-cp312-cp312-win32.whl", hash = "sha256:ec8a77f521a17506a24a5f626cb2aee7850f9b69a0afe704586f63a464f3cd64", size = 1025191 },
    { url = "https://files.pythonhosted.org/packages/92/29/06261ea000e2dc1e22907dbbc483a1093665509ea586b29b8986a0e56733/psycopg2_binary-2.9.10-cp312-cp312-win_amd64.whl", hash = "sha256:18c5ee682b9c6dd3696dad6e54cc7ff3a1a9020df6a5c0f861ef8bfd338c3ca0", size = 1164031 },
    { url = "https://files.pythonhosted.org/packages/3e/30/d41d3ba765609c0763505d565c4d12d8f3c79793f0d0f044ff5a28bf395b/psycopg2_binary-2.9.10-cp313-cp313-macosx_12_0_x86_64.whl", hash = "sha256:26540d4a9a4e2b096f1ff9cce51253d0504dca5a85872c7f7be23be5a53eb18d", size = 3044699 },
    { url = "https://files.pythonhosted.org/packages/35/44/257ddadec7ef04536ba71af6bc6a75ec05c5343004a7ec93006bee66c0bc/psycopg2_binary-2.9.10-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:e217ce4d37667df0bc1c397fdcd8de5e81018ef305aed9415c3b093faaeb10fb", size = 3275245 },
    { url = "https://files.pythonhosted.org/packages/1b/11/48ea1cd11de67f9efd7262085588790a95d9dfcd9b8a687d46caf7305c1a/psycopg2_binary-2.9.10-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:245159e7ab20a71d989da00f280ca57da7641fa2cdcf71749c193cea540a74f7", size = 2851631 },
    { url = "https://files.pythonhosted.org/packages/62/e0/62ce5ee650e6c86719d621a761fe4bc846ab9eff8c1f12b1ed5741bf1c9b/psycopg2_binary-2.9.10-cp313-cp313-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:3c4ded1a24b20021ebe677b7b08ad10bf09aac197d6943bfe6fec70ac4e4690d", size = 3082140 },
    { url = "https://files.pythonhosted.org/packages/27/ce/63f946c098611f7be234c0dd7cb1ad68b0b5744d34f68062bb3c5aa510c8/psycopg2_binary-2.9.10-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:3abb691ff9e57d4a93355f60d4f4c1dd2d68326c968e7db17ea96df3c023ef73", size = 3264762 },
    { url = "https://files.pythonhosted.org/packages/43/25/c603cd81402e69edf7daa59b1602bd41eb9859e2824b8c0855d748366ac9/psycopg2_binary-2.9.10-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8608c078134f0b3cbd9f89b34bd60a943b23fd33cc5f065e8d5f840061bd0673", size = 3020967 },
    { url = "https://files.pythonhosted.org/packages/5f/d6/8708d8c6fca531057fa170cdde8df870e8b6a9b136e82b361c65e42b841e/psycopg2_binary-2.9.10-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:230eeae2d71594103cd5b93fd29d1ace6420d0b86f4778739cb1a5a32f607d1f", size = 2872326 },
    { url = "https://files.pythonhosted.org/packages/ce/ac/5b1ea50fc08a9df82de7e1771537557f07c2632231bbab652c7e22597908/psycopg2_binary-2.9.10-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:bb89f0a835bcfc1d42ccd5f41f04870c1b936d8507c6df12b7737febc40f0909", size = 2822712 },
    { url = "https://files.pythonhosted.org/packages/c4/fc/504d4503b2abc4570fac3ca56eb8fed5e437bf9c9ef13f36b6621db8ef00/psycopg2_binary-2.9.10-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:f0c2d907a1e102526dd2986df638343388b94c33860ff3bbe1384130828714b1", size = 2920155 },
    { url = "https://files.pythonhosted.org/packages/b2/d1/323581e9273ad2c0dbd1902f3fb50c441da86e894b6e25a73c3fda32c57e/psycopg2_binary-2.9.10-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:f8157bed2f51db683f31306aa497311b560f2265998122abe1dce6428bd86567", size = 2959356 },
    { url = "https://files.pythonhosted.org/packages/08/50/d13ea0a054189ae1bc21af1d85b6f8bb9bbc5572991055d70ad9006fe2d6/psycopg2_binary-2.9.10-cp313-cp313-win_amd64.whl", hash = "sha256:27422aa5f11fbcd9b18da48373eb67081243662f9b46e6fd07c3eb46e4535142", size = 2569224 },
]

[[package]]
name = "repl-nix-workspace"
version = "0.1.0"
source = { virtual = "." }
dependencies = [
    { name = "email-validator" },
    { name = "flask" },
    { name = "flask-login" },
    { name = "flask-sqlalchemy" },
    { name = "flask-wtf" },
    { name = "gunicorn" },
    { name = "psycopg2-binary" },
    { name = "sqlalchemy" },
    { name = "werkzeug" },
]

[package.metadata]
requires-dist = [
    { name = "email-validator", specifier = ">=2.2.0" },
    { name = "flask", specifier = ">=3.1.0" },
    { name = "flask-login", specifier = ">=0.6.3" },
    { name = "flask-sqlalchemy", specifier = ">=3.1.1" },
    { name = "flask-wtf", specifier = ">=1.2.2" },
    { name = "gunicorn", specifier = ">=23.0.0" },
    { name = "psycopg2-binary", specifier = ">=2.9.10" },
    { name = "sqlalchemy", specifier = ">=2.0.38" },
    { name = "werkzeug", specifier = ">=3.1.3" },
]

[[package]]
name = "sqlalchemy"
version = "2.0.38"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "greenlet", marker = "(python_full_version < '3.14' and platform_machine == 'AMD64') or (python_full_version < '3.14' and platform_machine == 'WIN32') or (python_full_version < '3.14' and platform_machine == 'aarch64') or (python_full_version < '3.14' and platform_machine == 'amd64') or (python_full_version < '3.14' and platform_machine == 'ppc64le') or (python_full_version < '3.14' and platform_machine == 'win32') or (python_full_version < '3.14' and platform_machine == 'x86_64')" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/e4/08/9a90962ea72acd532bda71249a626344d855c4032603924b1b547694b837/sqlalchemy-2.0.38.tar.gz", hash = "sha256:e5a4d82bdb4bf1ac1285a68eab02d253ab73355d9f0fe725a97e1e0fa689decb", size = 9634782 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/00/6c/9d3a638f297fce288ba12a4e5dbd08ef1841d119abee9300c100eba00217/SQLAlchemy-2.0.38-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:bf89e0e4a30714b357f5d46b6f20e0099d38b30d45fa68ea48589faf5f12f62d", size = 2106330 },
    { url = "https://files.pythonhosted.org/packages/0e/57/d5fdee56f418491267701965795805662b1744de40915d4764451390536d/SQLAlchemy-2.0.38-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:8455aa60da49cb112df62b4721bd8ad3654a3a02b9452c783e651637a1f21fa2", size = 2096730 },
    { url = "https://files.pythonhosted.org/packages/42/84/205f423f8b28329c47237b7e130a7f93c234a49fab20b4534bd1ff26a06a/SQLAlchemy-2.0.38-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f53c0d6a859b2db58332e0e6a921582a02c1677cc93d4cbb36fdf49709b327b2", size = 3215023 },
    { url = "https://files.pythonhosted.org/packages/77/41/94a558d47bffae5a361b0cfb3721324ea4154829dd5432f80bd4cfeecbc9/SQLAlchemy-2.0.38-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b3c4817dff8cef5697f5afe5fec6bc1783994d55a68391be24cb7d80d2dbc3a6", size = 3214991 },
    { url = "https://files.pythonhosted.org/packages/74/a0/cc3c030e7440bd17ce67c1875f50edb41d0ef17b9c76fbc290ef27bbe37f/SQLAlchemy-2.0.38-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:c9cea5b756173bb86e2235f2f871b406a9b9d722417ae31e5391ccaef5348f2c", size = 3151854 },
    { url = "https://files.pythonhosted.org/packages/24/ab/8ba2588c2eb1d092944551354d775ef4fc0250badede324d786a4395d10e/SQLAlchemy-2.0.38-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:40e9cdbd18c1f84631312b64993f7d755d85a3930252f6276a77432a2b25a2f3", size = 3172158 },
    { url = "https://files.pythonhosted.org/packages/e0/73/2a3d6217e8e6abb553ed410ce5adc0bdec7effd684716f0fbaee5831d677/SQLAlchemy-2.0.38-cp311-cp311-win32.whl", hash = "sha256:cb39ed598aaf102251483f3e4675c5dd6b289c8142210ef76ba24aae0a8f8aba", size = 2076965 },
    { url = "https://files.pythonhosted.org/packages/a4/17/364a99c8c5698492c7fa40fc463bf388f05b0b03b74028828b71a79dc89d/SQLAlchemy-2.0.38-cp311-cp311-win_amd64.whl", hash = "sha256:f9d57f1b3061b3e21476b0ad5f0397b112b94ace21d1f439f2db472e568178ae", size = 2102169 },
    { url = "https://files.pythonhosted.org/packages/5a/f8/6d0424af1442c989b655a7b5f608bc2ae5e4f94cdf6df9f6054f629dc587/SQLAlchemy-2.0.38-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:12d5b06a1f3aeccf295a5843c86835033797fea292c60e72b07bcb5d820e6dd3", size = 2104927 },
    { url = "https://files.pythonhosted.org/packages/25/80/fc06e65fca0a19533e2bfab633a5633ed8b6ee0b9c8d580acf84609ce4da/SQLAlchemy-2.0.38-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:e036549ad14f2b414c725349cce0772ea34a7ab008e9cd67f9084e4f371d1f32", size = 2095317 },
    { url = "https://files.pythonhosted.org/packages/98/2d/5d66605f76b8e344813237dc160a01f03b987201e974b46056a7fb94a874/SQLAlchemy-2.0.38-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ee3bee874cb1fadee2ff2b79fc9fc808aa638670f28b2145074538d4a6a5028e", size = 3244735 },
    { url = "https://files.pythonhosted.org/packages/73/8d/b0539e8dce90861efc38fea3eefb15a5d0cfeacf818614762e77a9f192f9/SQLAlchemy-2.0.38-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e185ea07a99ce8b8edfc788c586c538c4b1351007e614ceb708fd01b095ef33e", size = 3255581 },
    { url = "https://files.pythonhosted.org/packages/ac/a5/94e1e44bf5bdffd1782807fcc072542b110b950f0be53f49e68b5f5eca1b/SQLAlchemy-2.0.38-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:b79ee64d01d05a5476d5cceb3c27b5535e6bb84ee0f872ba60d9a8cd4d0e6579", size = 3190877 },
    { url = "https://files.pythonhosted.org/packages/91/13/f08b09996dce945aec029c64f61c13b4788541ac588d9288e31e0d3d8850/SQLAlchemy-2.0.38-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:afd776cf1ebfc7f9aa42a09cf19feadb40a26366802d86c1fba080d8e5e74bdd", size = 3217485 },
    { url = "https://files.pythonhosted.org/packages/13/8f/8cfe2ba5ba6d8090f4de0e658330c53be6b7bf430a8df1b141c2b180dcdf/SQLAlchemy-2.0.38-cp312-cp312-win32.whl", hash = "sha256:a5645cd45f56895cfe3ca3459aed9ff2d3f9aaa29ff7edf557fa7a23515a3725", size = 2075254 },
    { url = "https://files.pythonhosted.org/packages/c2/5c/e3c77fae41862be1da966ca98eec7fbc07cdd0b00f8b3e1ef2a13eaa6cca/SQLAlchemy-2.0.38-cp312-cp312-win_amd64.whl", hash = "sha256:1052723e6cd95312f6a6eff9a279fd41bbae67633415373fdac3c430eca3425d", size = 2100865 },
    { url = "https://files.pythonhosted.org/packages/21/77/caa875a1f5a8a8980b564cc0e6fee1bc992d62d29101252561d0a5e9719c/SQLAlchemy-2.0.38-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:ecef029b69843b82048c5b347d8e6049356aa24ed644006c9a9d7098c3bd3bfd", size = 2100201 },
    { url = "https://files.pythonhosted.org/packages/f4/ec/94bb036ec78bf9a20f8010c807105da9152dd84f72e8c51681ad2f30b3fd/SQLAlchemy-2.0.38-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:9c8bcad7fc12f0cc5896d8e10fdf703c45bd487294a986903fe032c72201596b", size = 2090678 },
    { url = "https://files.pythonhosted.org/packages/7b/61/63ff1893f146e34d3934c0860209fdd3925c25ee064330e6c2152bacc335/SQLAlchemy-2.0.38-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:2a0ef3f98175d77180ffdc623d38e9f1736e8d86b6ba70bff182a7e68bed7727", size = 3177107 },
    { url = "https://files.pythonhosted.org/packages/a9/4f/b933bea41a602b5f274065cc824fae25780ed38664d735575192490a021b/SQLAlchemy-2.0.38-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8b0ac78898c50e2574e9f938d2e5caa8fe187d7a5b69b65faa1ea4648925b096", size = 3190435 },
    { url = "https://files.pythonhosted.org/packages/f5/23/9e654b4059e385988de08c5d3b38a369ea042f4c4d7c8902376fd737096a/SQLAlchemy-2.0.38-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:9eb4fa13c8c7a2404b6a8e3772c17a55b1ba18bc711e25e4d6c0c9f5f541b02a", size = 3123648 },
    { url = "https://files.pythonhosted.org/packages/83/59/94c6d804e76ebc6412a08d2b086a8cb3e5a056cd61508e18ddaf3ec70100/SQLAlchemy-2.0.38-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:5dba1cdb8f319084f5b00d41207b2079822aa8d6a4667c0f369fce85e34b0c86", size = 3151789 },
    { url = "https://files.pythonhosted.org/packages/b2/27/17f143013aabbe1256dce19061eafdce0b0142465ce32168cdb9a18c04b1/SQLAlchemy-2.0.38-cp313-cp313-win32.whl", hash = "sha256:eae27ad7580529a427cfdd52c87abb2dfb15ce2b7a3e0fc29fbb63e2ed6f8120", size = 2073023 },
    { url = "https://files.pythonhosted.org/packages/e2/3e/259404b03c3ed2e7eee4c179e001a07d9b61070334be91124cf4ad32eec7/SQLAlchemy-2.0.38-cp313-cp313-win_amd64.whl", hash = "sha256:b335a7c958bc945e10c522c069cd6e5804f4ff20f9a744dd38e748eb602cbbda", size = 2096908 },
    { url = "https://files.pythonhosted.org/packages/aa/e4/592120713a314621c692211eba034d09becaf6bc8848fabc1dc2a54d8c16/SQLAlchemy-2.0.38-py3-none-any.whl", hash = "sha256:63178c675d4c80def39f1febd625a6333f44c0ba269edd8a468b156394b27753", size = 1896347 },
]

[[package]]
name = "typing-extensions"
version = "4.12.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/df/db/f35a00659bc03fec321ba8bce9420de607a1d37f8342eee1863174c69557/typing_extensions-4.12.2.tar.gz", hash = "sha256:1a7ead55c7e559dd4dee8856e3a88b41225abfe1ce8df57b7c13915fe121ffb8", size = 85321 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/26/9f/ad63fc0248c5379346306f8668cda6e2e2e9c95e01216d2b8ffd9ff037d0/typing_extensions-4.12.2-py3-none-any.whl", hash = "sha256:04e5ca0351e0f3f85c6853954072df659d0d13fac324d0072316b67d7794700d", size = 37438 },
]

[[package]]
name = "werkzeug"
version = "3.1.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markupsafe" },
]
sdist = { url = "https://files.pythonhosted.org/packages/9f/69/83029f1f6300c5fb2471d621ab06f6ec6b3324685a2ce0f9777fd4a8b71e/werkzeug-3.1.3.tar.gz", hash = "sha256:60723ce945c19328679790e3282cc758aa4a6040e4bb330f53d30fa546d44746", size = 806925 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/52/24/ab44c871b0f07f491e5d2ad12c9bd7358e527510618cb1b803a88e986db1/werkzeug-3.1.3-py3-none-any.whl", hash = "sha256:54b78bf3716d19a65be4fceccc0d1d7b89e608834989dfae50ea87564639213e", size = 224498 },
]

[[package]]
name = "wtforms"
version = "3.2.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markupsafe" },
]
sdist = { url = "https://files.pythonhosted.org/packages/01/e4/633d080897e769ed5712dcfad626e55dbd6cf45db0ff4d9884315c6a82da/wtforms-3.2.1.tar.gz", hash = "sha256:df3e6b70f3192e92623128123ec8dca3067df9cfadd43d59681e210cfb8d4682", size = 137801 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/08/c9/2088fb5645cd289c99ebe0d4cdcc723922a1d8e1beaefb0f6f76dff9b21c/wtforms-3.2.1-py3-none-any.whl", hash = "sha256:583bad77ba1dd7286463f21e11aa3043ca4869d03575921d1a1698d0715e0fd4", size = 152454 },
]
