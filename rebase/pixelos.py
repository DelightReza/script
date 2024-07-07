import os

pixelos = [
    {
        "local_path": "device_motorola_sm6225-common",
        "remote_url": "https://github.com/PixelOS-Devices/device_motorola_sm6225-common",
        "remote_branch": "fourteen",
        "upstream_url": "https://github.com/LineageOS/android_device_motorola_sm6225-common",
        "upstream_branch": "lineage-21"
    },
    {
        "local_path": "vendor_motorola_sm6225-common",
        "remote_url": "https://github.com/PixelOS-Devices/vendor_motorola_sm6225-common",
        "remote_branch": "fourteen",
        "upstream_url": "https://github.com/TheMuppets/proprietary_vendor_motorola_sm6225-common",
        "upstream_branch": "lineage-21"
    },
    {
        "local_path": "kernel_motorola_sm6225",
        "remote_url": "https://github.com/PixelOS-Devices/kernel_motorola_sm6225",
        "remote_branch": "fourteen",
        "upstream_url": "https://github.com/LineageOS/android_kernel_motorola_sm6225",
        "upstream_branch": "lineage-21"
    },
    {
        "local_path": "device_motorola_guamp",
        "remote_url": "https://github.com/PixelOS-Devices/device_motorola_guamp",
        "remote_branch": "fourteen",
        "upstream_url": "https://github.com/LineageOS/android_device_motorola_guamp",
        "upstream_branch": "lineage-21"
    },
    {
        "local_path": "vendor_motorola_guamp",
        "remote_url": "https://github.com/PixelOS-Devices/vendor_motorola_guamp",
        "remote_branch": "fourteen",
        "upstream_url": "https://github.com/TheMuppets/proprietary_vendor_motorola_guamp",
        "upstream_branch": "lineage-21"
    }
]

# Cloning repositories, rebasing and pushing
for repo in pixelos:
    if os.path.exists(repo["local_path"]):
        os.system(f"cd {repo['local_path']} && git fetch {repo['upstream_url']} {repo['upstream_branch']} && git rebase FETCH_HEAD && git push {repo['remote_url']} --force {repo['remote_branch']} && cd .. && rm -rf {repo['local_path']}")
    else:
        os.system(f"git clone {repo['remote_url']} -b {repo['remote_branch']} {repo['local_path']}")
        os.system(f"cd {repo['local_path']} && git fetch {repo['upstream_url']} {repo['upstream_branch']} && git rebase FETCH_HEAD && git push {repo['remote_url']} --force {repo['remote_branch']} && cd .. && rm -rf {repo['local_path']}")
