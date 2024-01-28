import os
import sys
import pkg_resources
from wheel.bdist_wheel import bdist_wheel

# 获取 site-packages 路径
site_packages_path = next(p for p in sys.path if 'site-packages' in p)

# 获取已安装的模块列表
installed_modules = [dist.key for dist in pkg_resources.working_set]

# 遍历每个模块并将其打包为 wheel 文件
for module_name in installed_modules:
    module_path = os.path.join(site_packages_path, module_name)
    if os.path.isdir(module_path):
        # 构建 wheel 文件的输出路径
        wheel_path = os.path.join(site_packages_path, f"{module_name}.whl")

        # 创建 bdist_wheel 实例
        bdist = bdist_wheel(dist_dir=site_packages_path)

        # 设置输入路径
        bdist.root_is_pure = False
        bdist.plat_name = 'any'
        bdist.universal = True
        bdist.distribution.dist_files = []

        # 执行打包操作
        bdist.run()

        # 重命名生成的 wheel 文件
        os.rename(
            os.path.join(site_packages_path, "dist", f"{module_name}-none-any.whl"),
            wheel_path
        )

        # 清理临时文件
        os.remove(os.path.join(site_packages_path, "dist", "requires.txt"))
        os.rmdir(os.path.join(site_packages_path, "dist"))
        os.rmdir(os.path.join(site_packages_path, "build"))
