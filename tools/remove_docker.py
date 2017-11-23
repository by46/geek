from json import loads

import requests

content = """
[
  {
    "Id": "sha256:ed5fc67e2817f8b54a3763074d4c3834b9e74329940b437b06170b5e747efc8e",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.2.6"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:c913c9174ef813c21226c6def10d002b3b5d83a6a2c9b1e6f6e7788747c69277"
    ],
    "Created": 1509074767,
    "Size": 739157081,
    "VirtualSize": 739157081,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:2696ff7682db328edbc8ed3de23f4bf54b63ce8ac6b131d76109c1549cd55f76",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.2.5"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:ce394fafda42dcb14ddadf6fa2acd8d92c29cfe4300150968011f2b395aee4f1"
    ],
    "Created": 1509068687,
    "Size": 739157064,
    "VirtualSize": 739157064,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:70915b149dce3bbcafb8046b87903b2499c4656db412e376aacfb92a8f2f8afe",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.build228.b90d8"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:acbeda992017d3808ace5b14de1c64a89cc1f0e4d85f90bc29506472aa4f9dab"
    ],
    "Created": 1509009091,
    "Size": 403182480,
    "VirtualSize": 403182480,
    "Labels": {}
  },
  {
    "Id": "sha256:81133269c3b46492f7358098dbfaf055f6bfed29f9d8b3e6d9e2146ec5b378b4",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.build227.07e53"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:04034e7fbbe576d140719661687cf16c22b90d3f841a12dc0a7b814bc4fef050"
    ],
    "Created": 1509008304,
    "Size": 403182179,
    "VirtualSize": 403182179,
    "Labels": {}
  },
  {
    "Id": "sha256:7ccdd6d3571769c9f5aa565eecc687dd4c871cc3c526dc2f7930ccbca6e3b1b5",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.2.4"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:4d6e2d5e5fe70feb2e2e9cdda43da9c276ad949c1f90ecb8dc50b1e9be2a6aaf"
    ],
    "Created": 1509004690,
    "Size": 739157029,
    "VirtualSize": 739157029,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:664dbcd3ee8fc8b03d474ca29f00e24d402436a078b64fac9bc53f91cec468c3",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.build225.b65e0"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:71d419d6bf8a2b041e0811369f28b0120b8f79b32bea3a3e54f29134b482a327"
    ],
    "Created": 1508996854,
    "Size": 403175596,
    "VirtualSize": 403175596,
    "Labels": {}
  },
  {
    "Id": "sha256:32d37a58a96e0565e6856b3c30f2ac57453c6b0e03bd234fdae610cb6add413e",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.2.3"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:90536d6c430fd6a0bd401e7ec98f92ac3b4bb01e504edb7d8fa88c9e49732a7e"
    ],
    "Created": 1508746619,
    "Size": 739157031,
    "VirtualSize": 739157031,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:6b340d8dab765ce17d4dd98a15a43285624d83039030fe01de7746f3cb65dd5d",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.2.2"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:0f3b7383084bcad20d0325605e759796bbe64c6183dfb8f3556160396ff3753e"
    ],
    "Created": 1508734139,
    "Size": 739156942,
    "VirtualSize": 739156942,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:bc241cd085640bd3ca4b8486b81932de417819d0f1111666d5eccc7b84d05317",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.2.1"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:75f44d97810704de727d0ab2ad0ae9f784be9103660b0c40cb0aeaccb41b4afb"
    ],
    "Created": 1508489738,
    "Size": 739156174,
    "VirtualSize": 739156174,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:ca34bcab1f8239cdccfb91399a890c19d2b0eecb4c0096c9c7412c360a78861e",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.60"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:50ef38e5384f709abe4ee3c5a7afe1180d3fd60d4bb03b7e40a07fbaf6b31038"
    ],
    "Created": 1508400102,
    "Size": 739155920,
    "VirtualSize": 739155920,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:5e35f64036b87576837f04e8955e66a34997e0283eb9c38b825c04199256650c",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.59"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:5c5a313496da750dbb9336fb763a60d1015d66fbce60e060208d45ca04b1277e"
    ],
    "Created": 1508384375,
    "Size": 739155921,
    "VirtualSize": 739155921,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:e6403ae1d67f25114a62a551fb2b4514611e32b204036c9128ee3ad816b5f484",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.58"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:135ccfebe14248d4e0a3ce78c241df6a55dd044e1d947a7decb6015781e225a4"
    ],
    "Created": 1508229409,
    "Size": 739155618,
    "VirtualSize": 739155618,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:561d7f41d3e9028eee459160caa9c4547a84fc72a96b94f39f45673bf3b326d4",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ll/guanzhou:216"
    ],
    "RepoDigests": [
      "docker.neg/ll/guanzhou@sha256:84e87cca2c2a3383bf6036e8c355dfd36fc92d3c42915c1ee382c7c48af152b2"
    ],
    "Created": 1508224454,
    "Size": 192730304,
    "VirtualSize": 192730304,
    "Labels": {}
  },
  {
    "Id": "sha256:a65a933f3bb1a65a75ef4d4f62a6c5a242f06119d60ce0e024935b1b1c0241c3",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.57"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:38bf0e7d0b14c661a243952991642480f061db15e33b6f9b5efb5303b2a304fc"
    ],
    "Created": 1508139751,
    "Size": 739151336,
    "VirtualSize": 739151336,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:e011d52536cbde307f6ef9b11ad27facf1a568bb9b8006691312101e873672c2",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.56"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:b5df6463c8a6cf6a35ff273e1d82bdb2ee302387ddd355547a78c4a385732ada"
    ],
    "Created": 1507879592,
    "Size": 739151570,
    "VirtualSize": 739151570,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:7944330638a13c9c99fa2e09d0875394e5b8e0862a5a30d9b4b6b08744376137",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.55"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:c68fbd4ecff18389557c656a6298a5b38ab3fee97c6272433117d9276352104b"
    ],
    "Created": 1507786362,
    "Size": 739150722,
    "VirtualSize": 739150722,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:411fca6826d2be21a3e244e908b6843f359b03a9b23b97c99fee2577a5850472",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.54"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:dd93d45fa7a12a08a79d041f95df313966514277bd0c5f4c04b374f2ef37e9b4"
    ],
    "Created": 1507780262,
    "Size": 739150699,
    "VirtualSize": 739150699,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:a92f1675ca16123db1e9812d4b3f30ffb3badd75198d17965ab99fac79ab4919",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.53"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:c74cc9b39db8bf57947f9bd3a0dcd2de3f4e872c4da863646f6afaf52853a75c"
    ],
    "Created": 1507715118,
    "Size": 739150722,
    "VirtualSize": 739150722,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:15547b4560b2fc852a6161df481d03d7a5d317ca42162133bd2111f2c10afa04",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.build189.38f65"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:d654b54a1cb704ae9953039cb0daef76f32245bd80a7a2151073144f48be6d5f"
    ],
    "Created": 1507699258,
    "Size": 403136803,
    "VirtualSize": 403136803,
    "Labels": {}
  },
  {
    "Id": "sha256:bb1b6893ef28267b4e08a86eab71c42e2cb467f215456a819deecda0703aedc1",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release178.5304d"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:3da3943548ca0acb438ed1beb1e40ddb0cdf65ab2ed8f1a242daff5217e81202"
    ],
    "Created": 1507618778,
    "Size": 403148171,
    "VirtualSize": 403148171,
    "Labels": {}
  },
  {
    "Id": "sha256:1dce21224eb4aa5883e2c188902c6641e1a7f6861bd7fc5cc2f0f9ae73a63732",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release175.48a87"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:e40ad7d1eeb59b8a4992e1b90b705a5e8ffe7913f63d447d56144d6149cc5bc6"
    ],
    "Created": 1507616217,
    "Size": 403147692,
    "VirtualSize": 403147692,
    "Labels": {}
  },
  {
    "Id": "sha256:aa50ae906392a58bc7f5b012869b8671d778db9df2798f80f7350888ccb3ff95",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release173.dfa22"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:9f292920f57c0e5589074cbdf4b85f5e245376a817808151fa1dc27b749ac65c"
    ],
    "Created": 1507459302,
    "Size": 403237890,
    "VirtualSize": 403237890,
    "Labels": {}
  },
  {
    "Id": "sha256:44bc2b641d72da7aa9bdb68b8d70fd9c7156fb12b6342f0d8579b246f86538e0",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release172.7e93f"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:b51f7ce4e7ed0d87db80b55f660b054dddb34465d44cb5827a292fc4b0886c35"
    ],
    "Created": 1507443360,
    "Size": 403236517,
    "VirtualSize": 403236517,
    "Labels": {}
  },
  {
    "Id": "sha256:78018aa1a1e4ff05168ca20cb2c3a6a1f2dc91dfeff9a84da2e885127879afce",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release153.f8537"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:b2b764b460edcfb75786e955c3e7630646ac46a25834a3bf6ac0eb19dd2f33f5"
    ],
    "Created": 1507287595,
    "Size": 403189618,
    "VirtualSize": 403189618,
    "Labels": {}
  },
  {
    "Id": "sha256:3ba4828c0bccb60b61039b3499617ede749cda568b9f5727e2a58067778a7f2c",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.52"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:c21c6c1a43c5105f93cb0c5646f0cef70b40c6034ed52722a95b6268d3cdb3ce"
    ],
    "Created": 1507275930,
    "Size": 739150417,
    "VirtualSize": 739150417,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:26d052e0be2f3c9328eaa7337e50d92907779b9241b86231bafe157edf704a3f",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.51"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:7973b3d4be1870b41ea4302114ccc099438b5a097dcaa6521bed8007ae0516e4"
    ],
    "Created": 1507192197,
    "Size": 739150157,
    "VirtualSize": 739150157,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:cbf99e320569f4c80934be2a2103dd9f2fcbc0a751280bc49920a06a040ddc89",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.50"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:8b1c7ff9fe5839d0f7ef3ace73b3a64599c87bf431747a12381e094f0eb17a0c"
    ],
    "Created": 1507182551,
    "Size": 739150067,
    "VirtualSize": 739150067,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:65cfde2fa9cb1f44d4c8f6f10d6f2a69dd3b7aedf9dfa4d219ccb5228a06df61",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.49"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:cc445b429a330c3448599c0289bc2a28a51d577875f4539134ba1f6b525951c3"
    ],
    "Created": 1507175306,
    "Size": 739150485,
    "VirtualSize": 739150485,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:bb4486467720183e84358bd7b864cf642f858259ef911575204ba3c07a31d9ef",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.48"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:23cab228ad4dc8a5145e8c6ea2aefce2707f7af5ea09642e42974202a7f08bef"
    ],
    "Created": 1507023044,
    "Size": 739149668,
    "VirtualSize": 739149668,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:797a0d60b29dc760a7144cda9364cc609bcd9ab61a034bd7acc2ed711680dad8",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.47"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:53c4d41e408dfc7394b61f8f8a3aa2fdde18cc7952dbb56af6ba8dbce54487af"
    ],
    "Created": 1506933737,
    "Size": 739148399,
    "VirtualSize": 739148399,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:20610749e2f393af744b678c1265b80c588f13e6b32844aaba076a4cc6b192d8",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.46"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:9f0b4866d91a8b25fe70f854432d387e1dd1eece6ca3aae906f7316196e7323f"
    ],
    "Created": 1506929369,
    "Size": 739148374,
    "VirtualSize": 739148374,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:245cae0deb810d607946c475be642fbdd9e86cc33cb652725ef0504343dfa2cf",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.45"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:0a93744f3e9bc5824ea7c2317284a1cc03cfc54c2a7a0ad4a3ad7fd74c7f8c8b"
    ],
    "Created": 1506761334,
    "Size": 739147724,
    "VirtualSize": 739147724,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:299c4158815e7da529f710515724b04cbc40f8e98f2355973337821e30e247ca",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release150.7a86d"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:b6caf58172cebd43bff8fa5d930f28d04619feac905534bee1e0a224caae7b11"
    ],
    "Created": 1506756173,
    "Size": 403179620,
    "VirtualSize": 403179620,
    "Labels": {}
  },
  {
    "Id": "sha256:117be37a940837c41542a17935b8237546bb8385a9097bb5be870f094c387a7e",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release146.c882b"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:2499ecbb77c1f3bdc120ee09d338593f2336be305998f411e7fd46608668163c"
    ],
    "Created": 1506742146,
    "Size": 403153509,
    "VirtualSize": 403153509,
    "Labels": {}
  },
  {
    "Id": "sha256:ea47fe654551efbfc3d5890cc2fd4b7b18b4e0c425b1ead7e43b86f7c17c77ba",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release145.1ea3c"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:de07b50dc35ac3842a7f650391d1b284805df89c6bac48d36c928ca502ea36fe"
    ],
    "Created": 1506686723,
    "Size": 403150344,
    "VirtualSize": 403150344,
    "Labels": {}
  },
  {
    "Id": "sha256:f3738478f6537c9b22df3b40ddfb9f7f7d80b66fd9b1f15cf2939ea34d99b08b",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release144.034d7"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:0813c00cb15f58c3e54fcc2f41b6428c7866f2d76bef8f90e1f1d295abc3a53a"
    ],
    "Created": 1506685433,
    "Size": 403150364,
    "VirtualSize": 403150364,
    "Labels": {}
  },
  {
    "Id": "sha256:9bd1fa4e29155338090a48d4d39ec5f887b048beab63234a6d5315dab195414b",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release143.5af14"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:2ee3eb1e29fa5237665b7f09f99d2122253058a65c8782b0ceed421d368a1539"
    ],
    "Created": 1506682852,
    "Size": 403148281,
    "VirtualSize": 403148281,
    "Labels": {}
  },
  {
    "Id": "sha256:ebdabad6608d7c624c5b70225e7cb29699f96adbecdd5fc8e92aa1daa34c2c50",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release142.56adb"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:062e27b382d53dbfa6db1de12c437ecfe51e6ba50122e6cb21ec4c5864d4a708"
    ],
    "Created": 1506675895,
    "Size": 403149271,
    "VirtualSize": 403149271,
    "Labels": {}
  },
  {
    "Id": "sha256:4f26e0675541ee797ff62c1c1092a58edfce253062b4c5ac8adee010ced2b4dd",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.44"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:d2309bfca0040aeabeaf28f683dc25cff6b767986794a3f15c1f1ef9ea74e522"
    ],
    "Created": 1506675386,
    "Size": 739140119,
    "VirtualSize": 739140119,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:6b8d42c2add0aa0cebf97bf0bcda917dba2d734f4086d1cdc209e257a6901d14",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release141.eaeeb"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:eeaca4bd5f0700478b6483ad8ed6b5721b5a5edd1408f6ce7f17ee9c1a14b066"
    ],
    "Created": 1506663535,
    "Size": 403149276,
    "VirtualSize": 403149276,
    "Labels": {}
  },
  {
    "Id": "sha256:9b531a3e49032413534608f2beef76e733fe6c04f74b9eb0af729b7e464792c1",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release139.6fab6"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:7232f668d2a46027d18f5bf98004f22c16538a6f833c458c5d4f379dbe97b1de"
    ],
    "Created": 1506590949,
    "Size": 403145291,
    "VirtualSize": 403145291,
    "Labels": {}
  },
  {
    "Id": "sha256:ee844786d8c2612816abf0f37bc730fd584e1f3db1c13f3091efba16008bc758",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.43"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:2d743850af14e7d07a28c146bfdefe78445c91686cfc67453278892db4423ebc"
    ],
    "Created": 1506571384,
    "Size": 739138232,
    "VirtualSize": 739138232,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:4118eacab8450950fa1b41eb38dc231b0089d1ab8c748a9d9ac96c52631732f8",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release132.ed053"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:e1dc83469c9b62e7f24611a57067d02d07ff47dee2086fec3cdb73994d52eb20"
    ],
    "Created": 1506499510,
    "Size": 403136045,
    "VirtualSize": 403136045,
    "Labels": {}
  },
  {
    "Id": "sha256:6739e5e619d4f52d7f6daedf496191dc9b1c0a459b6596c2786a07aa3e50cfe8",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.42"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:1d86a976b12337b2631bbf2cdc20549f241a43935760109090354c4ba2445b84"
    ],
    "Created": 1506475825,
    "Size": 739135727,
    "VirtualSize": 739135727,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:c6249cb530bd9b921b527fe97ede34c3bd51c04224cf312dd0049da592f9d8bf",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.41"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:07eb8f4676aba35470ac7fed1d0ffaeac1fbebc7790b71b179a27bc84ab9ad4e"
    ],
    "Created": 1506417929,
    "Size": 739135781,
    "VirtualSize": 739135781,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:993922430690bbf5ad8f8e2658becd18aa7d182ebc3181fbc382255f446bf3e8",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release125.c6140"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:3ae6d41fbfde6cf7e64e51f15b14685519a1b49b50793f44dbaf1399ff5bbbe2"
    ],
    "Created": 1506310581,
    "Size": 403124546,
    "VirtualSize": 403124546,
    "Labels": {}
  },
  {
    "Id": "sha256:0834e796ae0bc76cbb4aca25843b83bf6721a3a20076af632df92520b9851949",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.40"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:b9ff8fb8c95eb9a33416784d483bbbf75a84045d125a6be58e86c95aadf0ff18"
    ],
    "Created": 1506306852,
    "Size": 739135074,
    "VirtualSize": 739135074,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:76fb692a33584884828b9e34b0f527db93f3858e79ceac340dc3dc28a5174363",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.39"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:1c09cdeec46f2ed67b0b8fbb1a2bdf22e51276b42573b75dadc2c0bb0a23fb4c"
    ],
    "Created": 1506070898,
    "Size": 739135068,
    "VirtualSize": 739135068,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:ec66aab48ef625943f94fcfd9eebb737671720e0dc68aeb79334a4531a09e77e",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.38"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:ec50b3079ed3c1c4ccd64a35232f49299daffd6307cf224339a6b970d722d17c"
    ],
    "Created": 1505809686,
    "Size": 739134809,
    "VirtualSize": 739134809,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:394dbc020291f769c86077530f90b1df86b31619c6a36110c4d45e6020842459",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.37"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:6f12b236735dbaabd380938ee103c0e3893e7abb0acdd3ca9db73d3ded87c7a8"
    ],
    "Created": 1505713680,
    "Size": 739135087,
    "VirtualSize": 739135087,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:82c8c1a8f5815b281e5aee37d8d2191f59bc38286ade4b5fb0bf53eb3f9324f9",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.36"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:8a04888221ff8f5a5f1672282b84ff74539218392209cd535d063f0d2fd76097"
    ],
    "Created": 1505457939,
    "Size": 739135015,
    "VirtualSize": 739135015,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:11704603550d43954752592312b30af518df589c199128de317e85f96d96f3cc",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/ecbd/loanaction:v0.1.35"
    ],
    "RepoDigests": [
      "docker.neg/ecbd/loanaction@sha256:8051320467434180c643922477efb50685fce8073d5bc8a54f3d57b8022954c5"
    ],
    "Created": 1505377284,
    "Size": 739134317,
    "VirtualSize": 739134317,
    "Labels": {
      "build-date": "20170315",
      "license": "GPLv2",
      "name": "CentOS Base Image",
      "vendor": "CentOS"
    }
  },
  {
    "Id": "sha256:563af81c07879fd3ce5d3bb7d4c8b3da7c6b97235ea47dd5b38a134247e92e6b",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_storage:0.0.1.release22.81f2e"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_storage@sha256:788cf37cab4180441e2fef3f42f856d79c4c0fec4de19efc658d3bd453b8cc26"
    ],
    "Created": 1499318106,
    "Size": 402995543,
    "VirtualSize": 402995543,
    "Labels": {}
  },
  {
    "Id": "sha256:41439acb14618d1e930cde988f37d270b5aea51738602a69684e175408d24c46",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_storage:0.0.1.release21.f46b2"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_storage@sha256:e6c7259563aaa188e976fe47ede40e81a8a5206a2cd1904719090206084853c9"
    ],
    "Created": 1499306410,
    "Size": 402995570,
    "VirtualSize": 402995570,
    "Labels": {}
  },
  {
    "Id": "sha256:f103b44723bb963efcfba398955cae0c61fb6a90ace6a878f39ea6567bebbded",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_storage:0.0.1.build20.2ab2d"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_storage@sha256:a16e0ef97769366129af2e6185f4efaf36a0df8dda8d932152b2d01cb1a3e669"
    ],
    "Created": 1499305744,
    "Size": 402995344,
    "VirtualSize": 402995344,
    "Labels": {}
  },
  {
    "Id": "sha256:d6328a82212e0df1f4472d59c9bb12ebcaa6ac8d5257acb4779df85e40d872f9",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release40.b0698"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:9c1e8d42c206f722e2ddec51128660942e36084e1f8d9bac3e448bb6074a70ff"
    ],
    "Created": 1499148700,
    "Size": 403046273,
    "VirtualSize": 403046273,
    "Labels": {}
  },
  {
    "Id": "sha256:f11bd8fad62f12be02968b56711d16b5ff757d0fea9b29a2e1cb3fe346d60857",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release39.fa4a7"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:34f0458320b790e2f9d911eed403846ff532ae64a97587082729ed6053e4b1b6"
    ],
    "Created": 1499137387,
    "Size": 403046251,
    "VirtualSize": 403046251,
    "Labels": {}
  },
  {
    "Id": "sha256:49cce9b47034d2cd67635d33f7f287ad8d1bfce0fdb0baeed0e7a904f2a48214",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release38.42030"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:07fff3ed31412d2e2963f14184548b2124f6520241c8b9524922b464baad776f"
    ],
    "Created": 1498890555,
    "Size": 403046248,
    "VirtualSize": 403046248,
    "Labels": {}
  },
  {
    "Id": "sha256:739b25de91bebdba1e594662307e154ea76b2bf47200526910f6f91f10cc6349",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_storage:0.0.1.release12.2c67c"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_storage@sha256:931abb9731e55f9164f662aee912fce322aad3c132aa3cf684c427832cda9281"
    ],
    "Created": 1498888202,
    "Size": 402993087,
    "VirtualSize": 402993087,
    "Labels": {}
  },
  {
    "Id": "sha256:336931b6ae74e67f655a21cad166319bb26fa13b8dc062bbb3f59634d66d0bc2",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release34.46beb"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:849981fe5d5698d3101c82c23967d544289b1ad2f6cf5b34fc30accb2e60ddd8"
    ],
    "Created": 1498875636,
    "Size": 403044621,
    "VirtualSize": 403044621,
    "Labels": {}
  },
  {
    "Id": "sha256:cc8fa08f44656f23dd40a3a080a8a80b7432b0807f6055cdb0b79d1264c4f5ab",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_storage:0.0.1.release10.0c8be"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_storage@sha256:023af896c500832063b7248e0731f7bc799c0ea1c429b453b79a879b2f1e35d8"
    ],
    "Created": 1498872287,
    "Size": 402991720,
    "VirtualSize": 402991720,
    "Labels": {}
  },
  {
    "Id": "sha256:f16819f41686293e28270e13ea74848cdddd4ccfca72d8ca709ef73b3ee1eaf7",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_storage:0.0.1.release9.54504"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_storage@sha256:9217f815757f3af12af146d44443615c72e55e6e419de490be70cacb46efa63f"
    ],
    "Created": 1498871674,
    "Size": 402991558,
    "VirtualSize": 402991558,
    "Labels": {}
  },
  {
    "Id": "sha256:8613bc81456576605fff74db01c82bb2c6c9043fc6c7116464a5103a55d3b7a7",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/dfis/attachment_api:0.0.1.release33.76e59"
    ],
    "RepoDigests": [
      "docker.neg/dfis/attachment_api@sha256:b1719f899b83b2f8c8129d29e515269529622e87928e9ca54a0a49ca8a8d823d"
    ],
    "Created": 1498788830,
    "Size": 403043308,
    "VirtualSize": 403043308,
    "Labels": {}
  },
  {
    "Id": "sha256:adf8ef6bda11f0c1ac4cc3adbd7746f865dafee2e4462a3dec0981e07997aa45",
    "ParentId": "",
    "RepoTags": [
      "docker.neg/bts/humpback-agent:1.1.0"
    ],
    "RepoDigests": [
      "docker.neg/bts/humpback-agent@sha256:05945d2c945c378e45980b3cf32635707c3ddb3145e011387747a9c225b53f38"
    ],
    "Created": 1474855124,
    "Size": 19659288,
    "VirtualSize": 19659288,
    "Labels": null
  }
]
"""

images = loads(content)
items = [(x['Id'][:14], x['RepoTags']) for x in images if 'attachment' in x['RepoTags'][0]]
headers = {'X-PROXY-IP': "172.16.171.24"}
for image_id, tags in items:
    print(image_id, tags)
    response = requests.delete('http://10.1.46.51:8502/dockerapi/v2/images/' + image_id, headers=headers)
    print response.status_code
