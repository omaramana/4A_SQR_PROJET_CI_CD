Les workflows crées sont les suivaants : 

Les workflows allerSurLeSite.yml, question3.yml et echoNewPush.yml ont été crées lors de la première séance de TD, ils ne servent à rien dans le cadre dans notre projet mais nous avons décidé de les garder. 

• Une déclenchée à chaque changement pour builder l’application. : buildApplication.yml 

![badge buildApplication](https://github.com/omaramana/4A_SQR_PROJET_CI_CD/actions/workflows/buildApplication.yml/badge.svg)

• Une déclenchée manuellement pour builder et dockeriser et pousser l’image de l’API. : bdpImageAPI.yml (bdp pour Build Docker et push) 

![badge bdpImageAPI](https://github.com/omaramana/4A_SQR_PROJET_CI_CD/actions/workflows/bdpImageAPI.yml/badge.svg)

• Une déclenchée pour chaque tag semver pour builder et dockeriser et pousser l’image de l’API avec en tag la version semver spécifiée. : Docker_Push_GCR.yml

![badge Docker_Push_GCR](https://github.com/omaramana/4A_SQR_PROJET_CI_CD/actions/workflows/Docker_Push_GCR.yml/badge.svg)
