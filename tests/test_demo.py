import time

import pytest

from lib.pages.LoginPage import LoginPage
from lib.pages.base import Base
from lib.pages.MenuPage import MenuPage
from lib.utils.Utils import Utils


@pytest.mark.TestDemo
class TestDemo(Base):
    ag_final_data = {}

    @pytest.mark.dependency(name="login")
    def test_login_valid_username_password(self, objects):
        """FO Login with valid username password"""

        login_page = LoginPage(objects)
        login_page.do_login(objects['config']['username'], objects['config']['password'])
        menu = MenuPage(objects)
        assert menu.is_login_success(), "Login Failed"

    # @pytest.mark.dependency(name="tc01", depends=["login"])
    # def test_add_ips(self, objects):
    #     """TC-01 : Add IP to Subscription"""
    #
    #     # Creates Obj
    #     menu = MenuPage(objects)
    #     assets = AssetsPage(objects)
    #     host_assets = HostAssetsPage(objects)
    #
    #     # Steps
    #     menu.go_to_assets()
    #     assets.go_to_host_asset()
    #     data = {
    #         "ips": objects['config']['ag_ips'],
    #         "tracking_method": "ip",
    #         "modules": ["PC", "Certview"]
    #     }
    #     host_assets.add_ip(data)
    #     host_assets.verify_datalist(data)
    #
    # @pytest.mark.dependency(name="tc02", depends=["login", "tc01"])
    # def test_create_asset_group_01(self, objects):
    #     """TC-02 : Create Asset Group with Title only"""
    #
    #     # Creates Obj
    #     menu = MenuPage(objects)
    #     assets = AssetsPage(objects)
    #     asset_group = AssetGroupPage(objects)
    #
    #     # Steps
    #     menu.go_to_assets()
    #     assets.go_to_asset_group()
    #     asset_group.go_to_create_new_asset_group()
    #     ag_data = {
    #         "title": "AG_UI_" + str(Utils.generate_random_number()),
    #     }
    #     TestDemo.ag_final_data.update(ag_data)
    #     asset_group.fill_data(ag_data)
    #     asset_group.click_on_save()
    #     asset_group.verify_datalist(ag_data)
    #     asset_group.verify_view_ag(ag_data)
    #     asset_group.click_on_edit_from_view()
    #     asset_group.verify_edit_ag(ag_data)
    #     asset_group.click_on_cancel()
    #
    # @pytest.mark.dependency(name="tc03", depends=["login", "tc01", "tc02"])
    # def test_upadate_asset_group_01(self, objects):
    #     """TC-03 : Update add Single IP to Asset Group """
    #
    #     # Creates Obj
    #     menu = MenuPage(objects)
    #     assets = AssetsPage(objects)
    #     asset_group = AssetGroupPage(objects)
    #
    #     # Steps
    #     menu.go_to_assets()
    #     assets.go_to_asset_group()
    #     update_ag_data = {
    #         "ips": objects['config']['ag_ips']
    #     }
    #     asset_group.edit_asset_group(TestDemo.ag_final_data["title"])
    #     tmp_data = asset_group.get_updated_ag_data(TestDemo.ag_final_data, update_ag_data)
    #     TestDemo.ag_final_data.update(tmp_data)
    #     print(TestDemo.ag_final_data)
    #     asset_group.fill_data_for_update(update_ag_data)
    #     asset_group.click_on_save()
    #     asset_group.verify_datalist(TestDemo.ag_final_data)
    #     asset_group.verify_view_ag(TestDemo.ag_final_data)
    #     asset_group.click_on_edit_from_view()
    #     asset_group.verify_edit_ag(TestDemo.ag_final_data)
    #     asset_group.click_on_cancel()
    #
    # @pytest.mark.dependency(name="tc04", depends=["login", "tc02"])
    # def test_delete_asset_group_01(self, objects):
    #     """TC-04 : Delete Asset Group"""
    #
    #     # Creates Obj
    #     menu = MenuPage(objects)
    #     assets = AssetsPage(objects)
    #     asset_group = AssetGroupPage(objects)
    #
    #     # Steps
    #     menu.go_to_assets()
    #     assets.go_to_asset_group()
    #     asset_group.delete_ag_with_title(TestDemo.ag_final_data["title"])
    #
    # @pytest.mark.dependency(name="tc05", depends=["login", "tc01"])
    # def test_remove_ips_01(self, objects):
    #     """TC-05 : Remove IPs"""
    #
    #     # Creates Obj
    #     menu = MenuPage(objects)
    #     assets = AssetsPage(objects)
    #     host_assets = HostAssetsPage(objects)
    #
    #     # Steps
    #     menu.go_to_assets()
    #     assets.go_to_host_asset()
    #     host_assets.delete_ips(objects['config']['ag_ips'])
    #     host_assets.verify_deleted_ips(objects['config']['ag_ips'])
