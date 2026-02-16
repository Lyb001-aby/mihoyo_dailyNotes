"""
米游社功能简单测试脚本 - 硬编码版
直接在代码里添加您的私人cookies
"""

import json
import sys
from miyoushe_func import (
    get_user_game_roles,
    get_user_game_roles_simple,
    format_roles_text,
    get_genshin_note,
    get_starrail_note,
    get_zzz_note,
    format_genshin_note,
    format_starrail_note,
    format_zzz_note
)


class MockLoginManager:
    """模拟的LoginManager"""
    def __init__(self):
        self.stoken = None
        self.mid = None
        self.account_id = None
        self.ltoken_v2 = None
        self.cookie_token_v2 = None
        self.ltoken = None
        self.cookie_token = None
        self.device_id1 = None
        self.device_fp1 = None
        self.device_id2 = None
        self.device_fp2 = None


def test_game_roles():
    """测试获取游戏角色"""
    print("\n" + "="*60)
    print("测试: 获取游戏角色信息")
    print("="*60)
    
    manager = MockLoginManager()
    
    # ===== 在这里修改你的登录凭证 =====
    manager.stoken = ""
    manager.mid = ""
    manager.account_id = ""
    
    # 设备信息（优先使用手机端）
    manager.device_id2 = ""
    manager.device_fp2 = ""
    # =================================
    
    print(f"SToken: {manager.stoken[:20]}..." if manager.stoken else "SToken: None")
    print(f"MID: {manager.mid[:10]}..." if manager.mid else "MID: None")
    print(f"Account ID: {manager.account_id}")
    print(f"Device ID: {manager.device_id2[:20]}..." if manager.device_id2 else "Device ID: None")
    
    if not all([manager.stoken, manager.mid, manager.account_id, manager.device_id2, manager.device_fp2]):
        print("\n❌ 请先在代码中填写登录凭证和设备信息")
        return
    
    print("\n正在获取游戏角色信息...")
    success, result = get_user_game_roles(manager)
    
    if success:
        print("\n✅ 获取成功!")
        print(f"共获取到 {len(result)} 个角色\n")
        
        # 显示详细信息
        for i, role in enumerate(result, 1):
            print(f"--- 角色 {i} ---")
            print(f"  游戏: {role.get('game_name', '未知')}")
            print(f"  昵称: {role.get('nickname', '未知')}")
            print(f"  UID: {role.get('game_uid', '未知')}")
            print(f"  等级: {role.get('level', 0)}")
            print(f"  服务器: {role.get('region_display', role.get('region', '未知'))}")
            print()
        
        # 尝试简化版本
        success_simple, simple_roles = get_user_game_roles_simple(manager)
        if success_simple:
            print("简化版本:")
            print(format_roles_text(simple_roles))
        
    else:
        print(f"\n❌ 获取失败: {result}")


def test_genshin_note():
    """测试原神实时便笺"""
    print("\n" + "="*60)
    print("测试: 原神实时便笺")
    print("="*60)
    
    manager = MockLoginManager()
    
    # ===== 在这里修改你的登录凭证 =====
    manager.stoken = ""
    manager.mid = ""
    manager.account_id = ""
    
    # V2凭证（必需）
    manager.ltoken_v2 = ""
    manager.cookie_token_v2 = ""
    
    # 设备信息
    manager.device_id2 = ""
    manager.device_fp2 = ""
    
    # 角色信息
    role_id = ""  # 角色UID
    server = "cn_gf01"  # 服务器: cn_gf01(天空岛) 或 cn_qd01(世界树)
    # =================================
    
    print(f"SToken: {manager.stoken[:20]}..." if manager.stoken else "SToken: None")
    print(f"MID: {manager.mid[:10]}..." if manager.mid else "MID: None")
    print(f"ltoken_v2: {'✓' if manager.ltoken_v2 else '✗'}")
    print(f"cookie_token_v2: {'✓' if manager.cookie_token_v2 else '✗'}")
    print(f"角色UID: {role_id}")
    print(f"服务器: {server}")
    
    required = [manager.stoken, manager.mid, manager.account_id, 
                manager.ltoken_v2, manager.cookie_token_v2,
                manager.device_id2, manager.device_fp2, role_id]
    
    if not all(required):
        print("\n❌ 请先在代码中填写所有必要信息")
        return
    
    print("\n正在获取原神实时便笺...")
    success, result = get_genshin_note(manager, role_id, server)
    
    if success:
        print("\n✅ 获取成功!")
        print(format_genshin_note(result))
    else:
        print(f"\n❌ 获取失败: {result}")


def test_starrail_note():
    """测试星穹铁道实时便笺"""
    print("\n" + "="*60)
    print("测试: 星穹铁道实时便笺")
    print("="*60)
    
    manager = MockLoginManager()
    
    # ===== 在这里修改你的登录凭证 =====
    manager.stoken = ""
    manager.mid = ""
    manager.account_id = ""
    
    # V2凭证（必需）
    manager.ltoken_v2 = ""
    manager.cookie_token_v2 = ""
    
    # 设备信息
    manager.device_id2 = ""
    manager.device_fp2 = ""
    
    # 角色信息
    role_id = ""  # 角色UID
    server = "prod_gf_cn"  # 服务器: prod_gf_cn(星穹列车)
    # =================================
    
    print("\n正在获取星穹铁道实时便笺...")
    success, result = get_starrail_note(manager, role_id, server)
    
    if success:
        print("\n✅ 获取成功!")
        print(format_starrail_note(result))
    else:
        print(f"\n❌ 获取失败: {result}")


def test_zzz_note():
    """测试绝区零实时便笺"""
    print("\n" + "="*60)
    print("测试: 绝区零实时便笺")
    print("="*60)
    
    manager = MockLoginManager()
    
    # ===== 在这里修改你的登录凭证 =====
    manager.stoken = ""
    manager.mid = ""
    manager.account_id = ""
    
    # V2凭证（必需）
    manager.ltoken_v2 = ""
    manager.cookie_token_v2 = ""
    
    # 设备信息
    manager.device_id2 = ""
    manager.device_fp2 = ""
    
    # 角色信息
    role_id = ""  # 角色UID
    server = "prod_gf_cn"  # 服务器: prod_gf_cn(新艾利都)
    # =================================
    
    print("\n正在获取绝区零实时便笺...")
    success, result = get_zzz_note(manager, role_id, server)
    
    if success:
        print("\n✅ 获取成功!")
        print(format_zzz_note(result))
    else:
        print(f"\n❌ 获取失败: {result}")


def test_from_full_cookie():
    """从完整Cookie测试"""
    print("\n" + "="*60)
    print("测试: 从完整Cookie解析")
    print("="*60)
    
    # ===== 在这里粘贴完整的Cookie字符串 =====
    cookie_str = """
    stoken=; 
    mid=; 
    account_id=; 
    ltoken_v2=; 
    cookie_token_v2=; 
    device_id_phone=; 
    device_fp_phone=
    """
    # ========================================
    
    # 解析Cookie
    cookies = {}
    for item in cookie_str.replace('\n', '').split(';'):
        item = item.strip()
        if '=' in item:
            key, value = item.split('=', 1)
            cookies[key.strip()] = value.strip()
    
    manager = MockLoginManager()
    manager.stoken = cookies.get('stoken')
    manager.mid = cookies.get('mid')
    manager.account_id = cookies.get('account_id') or cookies.get('ltuid')
    manager.ltoken_v2 = cookies.get('ltoken_v2')
    manager.cookie_token_v2 = cookies.get('cookie_token_v2')
    manager.device_id2 = cookies.get('device_id_phone')
    manager.device_fp2 = cookies.get('device_fp_phone')
    
    print("解析结果:")
    print(f"  SToken: {manager.stoken[:20]}..." if manager.stoken else "  SToken: None")
    print(f"  MID: {manager.mid[:10]}..." if manager.mid else "  MID: None")
    print(f"  Account ID: {manager.account_id}")
    print(f"  ltoken_v2: {'✓' if manager.ltoken_v2 else '✗'}")
    print(f"  cookie_token_v2: {'✓' if manager.cookie_token_v2 else '✗'}")
    
    if not all([manager.stoken, manager.mid, manager.device_id2, manager.device_fp2]):
        print("\n❌ Cookie解析不完整，缺少必要字段")
        return
    
    # 测试获取角色
    print("\n测试获取游戏角色...")
    success, result = get_user_game_roles(manager)
    if success:
        print(f"✅ 成功! 获取到 {len(result)} 个角色")
        for role in result:
            print(f"  - {role.get('game_name')}: {role.get('nickname')} (UID: {role.get('game_uid')})")
    else:
        print(f"❌ 失败: {result}")


def main():
    """主菜单"""
    while True:
        print("\n" + "="*60)
        print("米游社功能测试 - 硬编码版")
        print("="*60)
        print("1. 测试获取游戏角色")
        print("2. 测试原神实时便笺")
        print("3. 测试星穹铁道实时便笺")
        print("4. 测试绝区零实时便笺")
        print("5. 从完整Cookie测试")
        print("0. 退出")
        print("="*60)
        
        choice = input("请选择测试项 (0-5): ").strip()
        
        if choice == '1':
            test_game_roles()
        elif choice == '2':
            test_genshin_note()
        elif choice == '3':
            test_starrail_note()
        elif choice == '4':
            test_zzz_note()
        elif choice == '5':
            test_from_full_cookie()
        elif choice == '0':
            print("退出测试")
            break
        else:
            print("无效选择，请重新输入")
        
        input("\n按Enter键继续...")


if __name__ == "__main__":
    main()
