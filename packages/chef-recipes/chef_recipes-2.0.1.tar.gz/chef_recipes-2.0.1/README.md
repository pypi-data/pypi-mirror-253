# 👨‍🍳 Chef

A simple, customizable recipe management app.

A simple FastAPI + SQLAlchemy app + VueJS frontend.
Frontend app is built and bundled together with the python build downloadable from PyPI -> the entire app can be run with a single command.
It's also built as a single container and can be easily hosted (with little tweaks) on GCP Cloud Run.


<details>

<summary>Screenshots</summary>


<picture><img alt="screenshot1" src="https://github.com/jonasbrauer/chef/assets/10963153/7caf01e0-c1f6-487b-9b09-2483cf938161" height=360></picture>
<picture><img alt="screenshot2" src="https://github.com/jonasbrauer/chef/assets/10963153/067c5953-79cf-4be5-a2ca-89a293d3db90" height=360></picture>
<picture><img alt="screenshot3" src="https://github.com/jonasbrauer/chef/assets/10963153/3d237a3f-a3c8-4bd9-afad-43ac4ef57811" height=360></picture>
<picture><img alt="screenshot4" src="https://github.com/jonasbrauer/chef/assets/10963153/002aad12-4e6c-4815-8793-e6125405d940" height=360></picture>  |

</details>

## Installation

```shell
curl https://raw.githubusercontent.com/xyzjonas/chef/master/install.sh | bash
```

or install the package yourself

```shell
pip install chef-recipes
chef
```


or run with docker:

```shell
docker build . -t chef
docker run -p 8000:8000 -v ~/.chef:/chef/data chef
```


...or run on GCP using `scotch3840/misc:chef-gcp` image (PostgreSQL):
> ! second generation execution environment required.
- `BUCKET`: name of your GCP/CloudStorage bucket.
- `MNT_DIR`: target where the bucket will be mounted.
- `IMAGES_FOLDER`: where the app will be looking for and storing uploaded images, has to be somewhere inside your bucket.
- `DATABASE_URI`: specify your posgres or possibly put an sqlite file in the bucket as well.


## Build
### 1. With Docker

```shell
docker build . -t chef
```

### 2. Without Docker
```shell
cd ./src/js/chef
npm run build
cd -
poetry build
```