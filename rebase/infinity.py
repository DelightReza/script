import os

infinity = [
    {
        "local_path": "device_motorola_sm6225-common",
        "remote_url": "https://github.com/Infinity-X-Devices/device_motorola_sm6225-common",
        "remote_branch": "14",
        "upstream_url": "https://github.com/LineageOS/android_device_motorola_sm6225-common",
        "upstream_branch": "lineage-21"
    },
    {
        "local_path": "kernel_motorola_sm6225",
        "remote_url": "https://github.com/Infinity-X-Devices/kernel_motorola_sm6225",
        "remote_branch": "14",
        "upstream_url": "https://github.com/moto-guamp/android_kernel_motorola_sm6225",
        "upstream_branch": "lineage-21"
    },
    {
        "local_path": "device_motorola_guamp",
        "remote_url": "https://github.com/Infinity-X-Devices/device_motorola_guamp",
        "remote_branch": "14",
        "upstream_url": "https://github.com/LineageOS/android_device_motorola_guamp",
        "upstream_branch": "lineage-21"
    },
    {
        "local_path": "device_motorola_guam",
        "remote_url": "https://github.com/Infinity-X-Devices/device_motorola_guam",
        "remote_branch": "14",
        "upstream_url": "https://github.com/LineageOS/android_device_motorola_guam",
        "upstream_branch": "lineage-21"
    },
    {
        "local_path": "device_motorola_borneo",
        "remote_url": "https://github.com/Infinity-X-Devices/device_motorola_borneo",
        "remote_branch": "14",
        "upstream_url": "https://github.com/LineageOS/android_device_motorola_borneo",
        "upstream_branch": "lineage-21"
    },
    {
        "local_path": "device_motorola_devon",
        "remote_url": "https://github.com/Infinity-X-Devices/device_motorola_devon",
        "remote_branch": "14",
        "upstream_url": "https://github.com/LineageOS/android_device_motorola_devon",
        "upstream_branch": "lineage-21"
    },
    {
        "local_path": "device_motorola_hawao",
        "remote_url": "https://github.com/Infinity-X-Devices/device_motorola_hawao",
        "remote_branch": "14",
        "upstream_url": "https://github.com/LineageOS/android_device_motorola_hawao",
        "upstream_branch": "lineage-21"
    },
    {
        "local_path": "device_motorola_rhode",
        "remote_url": "https://github.com/Infinity-X-Devices/device_motorola_rhode",
        "remote_branch": "14",
        "upstream_url": "https://github.com/LineageOS/android_device_motorola_rhode",
        "upstream_branch": "lineage-21"
    },
    {
        "local_path": "device_motorola_cebu",
        "remote_url": "https://github.com/Infinity-X-Devices/device_motorola_cebu",
        "remote_branch": "14",
        "upstream_url": "https://github.com/RazaDroidProject/android_device_motorola_cebu",
        "upstream_branch": "lineage-21"
    }
]

# Cloning repositories, rebasing and pushing
for repo in infinity:
    if os.path.exists(repo["local_path"]):
        os.system(f"cd {repo['local_path']} && git fetch {repo['upstream_url']} {repo['upstream_branch']} && git rebase FETCH_HEAD && git push {repo['remote_url']} --force {repo['remote_branch']} && cd .. && rm -rf {repo['local_path']}")
    else:
        os.system(f"git clone {repo['remote_url']} -b {repo['remote_branch']} {repo['local_path']}")
        os.system(f"cd {repo['local_path']} && git fetch {repo['upstream_url']} {repo['upstream_branch']} && git rebase FETCH_HEAD && git push {repo['remote_url']} --force {repo['remote_branch']} && cd .. && rm -rf {repo['local_path']}")
