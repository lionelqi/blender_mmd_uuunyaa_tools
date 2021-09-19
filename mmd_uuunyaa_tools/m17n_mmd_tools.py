# -*- coding: utf-8 -*-
# Copyright 2021 UuuNyaa <UuuNyaa@gmail.com>
# This file is part of MMD UuuNyaa Tools.

import bpy

from mmd_uuunyaa_tools import REGISTER_HOOKS, UNREGISTER_HOOKS
from mmd_uuunyaa_tools.utilities import get_preferences


def initialize_mmd_tools_translation():
    preferences = get_preferences()

    if preferences.mmd_tools_translation_enabled:
        bpy.app.translations.register(__name__, translation_dict)


def finalize_mmd_tools_translation():
    preferences = get_preferences()

    if preferences.mmd_tools_translation_enabled:
        bpy.app.translations.unregister(__name__)

REGISTER_HOOKS.append(initialize_mmd_tools_translation)
UNREGISTER_HOOKS.append(finalize_mmd_tools_translation)

translation_dict = {
    "ja_JP": {
        # Preferences
        ("*", "View3D > Tool Shelf > MMD Tools Panel"): "3Dビュー > サイドバー > MMD Toolsパネル",
        ("*", "Utility tools for MMD model editing. (powroupi's forked version)"): "MMDモデル編集用のユーティリティーツールです。(powroupiのフォーク版)",
        ("*", "Shared Toon Texture Folder"): "共有トゥーンテクスチャフォルダ",
        ("*", "Base Texture Folder"): "ベーステクスチャフォルダ",
        ("*", "Dictionary Folder"): "辞書フォルダ",
        ("*", "Non-Collision Threshold"): "非コリジョンしきい値",

        # 3D Viewport > Sidebar > MMD > Operator Panel
        ("Operator", "Create Model"): "モデルを作成",
        ("Operator", "Create a MMD Model Root Object"): "MMDモデルルートオブジェクトを作成",
        ("*", "Name(Eng)"): "名前(英語)",

        ("Operator", "Convert Model"): "モデルを変換",
        ("Operator", "Convert to a MMD Model"): "MMDモデルへ変換",
        ("*", "Ambient Color Source"): "アンビエントカラーソース",
        ("*", "Edge Threshold"): "輪郭しきい値",
        ("*", "Minimum Edge Alpha"): "最小輪郭アルファ",

        ("Operator", "Convert Materials For Cycles"): "マテリアルをCycles用に変換",
        ("*", "Convert to Principled BSDF"): "プリンシプルBSDFへ変換",
        ("*", "Clean Nodes"): "ノードをクリーン",
        ("Operator", "Separate By Materials"): "マテリアルで分解",
        ("*", "Clean Shape Keys"): "シェイプキーをクリーン",
        ("Operator", "Join Meshes"): "メッシュを統合",
        ("*", "Sort Shape Keys"): "シェイプキーをソート",
        ("Operator", "Attach Meshes to Model"): "メッシュをモデルに取付",
        ("Operator", "Translation"): "翻訳",
        ("Operator", "Translate a MMD Model"): "MMDモデルを翻訳",
        ("*", "Dictionary"): "辞書",
        ("*", "Modes"): "モード",
        ("*", "MMD Names"): "MMD名",
        ("*", "Blender Names"): "Blender名",
        ("*", "Use Morph Prefix"): "モーフ接頭辞を使用",
        ("*", "Allow Fails"): "失敗を許可",

        ("*", "Bone Constraints:"): "ボーンコンストレイント:",
        ("*", "Physics:"): "物理演算:",
        ("Operator", "Build"): "構築",
        ("*", "Edge Preview:"): "輪郭プレビュー:",
        ("*", "Create"): "生成",
        ("*", "Clean"): "クリーン",
        ("*", "Model:"): "モデル:",

        ("Operator", "Import"): "インポート",
        ("*", "Types"): "タイプ",
        ("*", "Morphs"): "モーフ",
        ("*", "Clean Model"): "モデルをクリーン",
        ("*", "Fix IK Links"): "IKリンクを修正",
        ("*", "Apply Bone Fixed Axis"): "ボーン修正回転軸を適用",
        ("*", "Rename Bones - L / R Suffix"): "ボーンをリネーム - L / R接尾辞",
        ("*", "Rename Bones - Use Underscore"): "ボーンをリネーム - アンダースコア使用",
        ("*", "Rename Bones To English"): "ボーンを英語にリネーム",
        ("*", "Internal Dictionary"): "内蔵辞書",
        ("*", "use MIP maps for UV textures"): "UVテクスチャへミップマップを使用",
        ("*", "influence of .sph textures"): ".sphテクスチャの影響度",
        ("*", "influence of .spa textures"): ".spaテクスチャの影響度",
        ("*", "Log level"): "ログレベル",
        ("*", "Create a log file"): "ログファイルを作成",
        ("*", "Copy textures"): "テクスチャをコピー",
        ("*", "Sort Materials"): "マテリアルをソート",
        ("*", "Disable SPH/SPA"): "SPH/SPAを無効化",
        ("*", "Visible Meshes Only"): "可視メッシュのみ",
        ("*", "Sort Vertices"): "頂点をソート",

        ("*", "Motion:"): "モーション:",
        ("*", "Bone Mapper"): "ボーンマッパー",
        ("*", "Renamed bones"): "リネームしたボーン",
        ("*", "Treat Current Pose as Rest Pose"): "現在のポーズをレストポーズとして処理",
        ("*", "Mirror Motion"): "モーションをミラー",
        ("*", "Update scene settings"): "シーン設定を更新",
        ("*", "Use Frame Range"): "フレーム範囲を使用",

        ("*", "Pose:"): "ポーズ:",
        ("*", "Current Pose"): "現在のポーズ",
        ("*", "Active Pose"): "アクティブなポーズ",
        ("*", "All Poses"): "全てのポーズ",

        # 3D Viewport > Sidebar > MMD > Display Panel
        ("*", "Display Panel"): "表示パネル",
        ("Operator", "Bone"): "ボーン",
        ("Operator", "Morph"): "モーフ",
        ("Operator", "Add Display Item Frame"): "表示項目フレームを追加",
        ("Operator", "Remove Display Item Frame"): "表示項目フレームを削除",
        ("Operator", "Move Display Item Frame"): "表示項目フレームを移動",
        ("Operator", "Add Display Item"): "表示項目を追加",
        ("Operator", "Remove Display Item"): "表示項目を削除",
        ("Operator", "Move Display Item"): "表示項目を移動",
        ("*", "Quick setup display items"): "表示項目のクイックセットアップ",
        ("*", "Load Facial Items"): "表情項目をロード",
        ("*", "Load Bone Groups"): "ボーングループをロード",
        ("*", "Apply Bone Groups"): "ボーングループを適用",
        ("Operator", "Move To Top"): "最初へ移動",
        ("Operator", "Move To Bottom"): "最後へ移動",
        ("Operator", "Delete All"): "全て削除",

        # 3D Viewport > Sidebar > MMD > Morph Tools Panel
        ("*", "Morph Tools"): "モーフツール",
        ("*", "Eye"): "目",
        ("*", "Eye Brow"): "眉毛",
        ("*", "Mouth"): "口",
        ("Operator", "Add Morph"): "モーフを追加",
        ("Operator", "Remove Morph"): "モーフを削除",
        ("Operator", "Copy Morph"): "モーフをコピー",
        ("Operator", "Move Morph"): "モーフを移動",
        ("Operator", "Add Morph Offset"): "モーフオフセットを追加",
        ("Operator", "Remove Morph Offset"): "モーフオフセットを削除",
        ("*", "Related Mesh"): "関連するメッシュ",
        ("Operator", "Create Work Material"): "ワークマテリアルを生成",
        ("Operator", "Init Material Offset"): "マテリアルオフセットを初期化",
        ("*", "Texture factor"): "テクスチャ係数",
        ("*", "Sphere Texture factor"): "スフィアテクスチャ係数",
        ("*", "Toon Texture factor"): "トゥーンテクスチャ係数",

        # 3D Viewport > Sidebar > MMD > Rigid Bodies
        ("*", "Rigid Bodies"): "リジッドボディ",
        ("*", "Active Model"): "選択中のモデル",
        ("*", "All Models"): "全てのモデル",
        ("Operator", "Select Similar..."): "類似を選択...",
        ("*", "Collision Group"): "コリジョングループ",
        ("*", "Collision Group Mask"): "コリジョングループマスク",
        ("*", "Rigid Type"): "リジッドタイプ",
        ("*", "Hide Others"): "他を隠す",

        # 3D Viewport > Sidebar > MMD > Joints
        ("*", "Joints"): "ジョイント",
        ("Operator", "Add Joint"): "ジョイントを追加",
        ("Operator", "Remove Joint"): "ジョイントを削除",

        # 3D Viewport > Sidebar > MMD > Material Sorter Panel
        ("*", "Material Sorter"): "マテリアル順序",
        ("*", "Select a mesh object"): "メッシュを選択してください",
        ("*", "Use the arrows to sort"): "矢印を使って並べ替えてください",
        ("Operator", "Move Material Up"): "マテリアルを移動",
        ("Operator", "Move Material Down"): "マテリアルを移動",

        # 3D Viewport > Sidebar > MMD > Meshes Sorter Panel
        ("*", "Meshes Sorter"): "メッシュ順序",
        ("*", "Select a MMD Model"): "MMDモデルを選択してください",
        ("Operator", "Move Object"): "オブジェクトを移動",

        # 3D Viewport > Sidebar > MMD > Bone Order Panel
        ("*", "Bone Order"): "ボーン順序",
        ("*", "After Dynamics"): "物理後",
        ("*", "Transform Order"): "変形階層",

        # 3D Viewport > Sidebar > Misc > MMD Display Panel
        ("*", "MMD Display"): "MMD表示",
        ("*", "Temporary Object"): "テンポラリオブジェクト",
        ("*", "Rigid Body Name"): "リジッドボティ名",
        ("*", "Joint"): "ジョイント",
        ("*", "Joint Name"): "ジョイント名",
        ("*", "Toon Texture"): "トゥーンテクスチャ",
        ("*", "Sphere Texture"): "スフィアテクスチャ",
        ("*", "Property Drivers"): "プロパティドライバー",

        # 3D Viewport > Sidebar > Misc > MMD Shading Panel
        ("*", "MMD Shading"): "MMDシェーディング",
        ("Operator", "Shadeless"): "影なし",

        # 3D Viewport > Sidebar > Misc > MMD SDEF Driver Panel
        ("*", "MMD SDEF Driver"): "MMD SDEFドライバー",
        ("Operator", "Bind"): "バインド",
        ("Operator", "Unbind"): "アンバインド",
        ("*", "Bind SDEF Driver"): "SDEFドライバーをバインド",
        ("*", "- Auto -"): "自動",
        ("*", "Bulk"): "バルク",
        ("*", "Skip"): "スキップ",

        # Properties > Object Properties > MMD Lamp Tools
        ("*", "MMD Lamp Tools"): "MMD照明ツール",
        ("Operator", "Convert to MMD Lamp"): "MMD照明へ変換",
        ("*", "Light Source"): "光源",

        # Properties > Object Properties > MMD Camera Tools
        ("*", "MMD Camera Tools"): "MMDカメラツール",
        ("Operator", "Convert to MMD Camera"): "MMDカメラへ変換",
        ("*", "Camera Source"): "カメラソース",

        # Properties > Object Properties > MMD Model Information Panel
        ("*", "MMD Model Information"): "MMDモデル情報",
        ("*", "Name (English)"): "名前(英語)",
        ("*", "Comment (English)"): "コメント(英語)",
        ("Operator", "Change MMD IK Loop Factor"): "MMD IK反復係数を変更",
        ("*", "MMD IK Loop Factor"): "MMD IK反復係数",
        ("Operator", "Recalculate bone roll"): "ボーンロールを再計算",
        ("*", "This operation will break existing f-curve/action."): "この操作は既存のFカーブ/アクションを破壊します。",
        ("*", "Click [OK] to run the operation."): "[OK]をクリックして操作を実行してください。",

        # Properties > Object Properties > MMD Rigid Body
        ("*", "MMD Rigid Body"): "MMDリジッドボディ",
        ("*", "Physics + Bone"): "物理演算 + ボーン",
        ("*", "Collision Group Mask:"): "コリジョングループマスク:",

        # Properties > Object Properties > MMD Joint
        ("*", "MMD Joint"): "MMDジョイント",
        ("*", "X-Axis:"): "X軸:",
        ("*", "Y-Axis:"): "Y軸:",
        ("*", "Z-Axis:"): "Z軸:",
        ("*", "Spring(Linear)"): "スプリング(リニア)",
        ("*", "Spring(Angular)"): "スプリング(角度)",

        # Properties > Material Properties > MMD Material Panel
        ("*", "MMD Material"): "MMDマテリアル",
        ("*", "Color:"): "カラー:",
        ("*", "Shadow:"): "シャドウ:",
        ("*", "Double Sided"): "両面表示",
        ("*", "Ground Shadow"): "地面シャドウ",
        ("*", "Self Shadow Map"): "セルフシャドウマップ",
        ("*", "Self Shadow"): "セルフシャドウ",
        ("*", "Toon Edge"): "トゥーン輪郭",
        ("*", "Edge Color"): "輪郭カラー",
        ("*", "Edge Weight"): "輪郭ウェイト",

        # Properties > Material Properties > MMD Texture Panel
        ("*", "MMD Texture"): "MMDテクスチャ",
        ("*", "Texture:"): "テクスチャ:",
        ("*", "Sphere Texture:"): "スフィアテクスチャ:",
        ("*", "SubTexture"): "サブテクスチャ",
        ("*", "Use Shared Toon Texture"): "共有トゥーンテクスチャを使用",
        ("*", "Shared Toon Texture"): "共有トゥーンテクスチャ",

        # Properties > Bone Properties > MMD Bone Tools Panel
        ("*", "MMD Bone Tools"): "MMDボーンツール",
        ("*", "Information:"): "情報:",
        ("*", "Controllable"): "操作",
        ("*", "Tip Bone"): "ティップボーン",
        ("*", "Fixed Axis"): "軸制限",
        ("*", "Local Axes"): "ローカル軸",
        ("*", "Local X-Axis"): "ローカルX軸",
        ("*", "Local Z-Axis"): "ローカルZ軸",
        ("*", "Rotate +"): "回転 +",
        ("*", "Move +"): "移動 +",

        # Shader Editor > Shader Nodes
        ("*", "Base Tex Fac"): "ベーステクスチャ係数",
        ("*", "Base Tex"): "ベーステクスチャ",
        ("*", "Base Alpha"): "ベースアルファ",
        ("*", "Base UV"): "ベースUV",
        ("*", "Toon Tex Fac"): "トゥーンテクスチャ係数",
        ("*", "Toon Tex"): "トゥーンテクスチャ",
        ("*", "Toon Alpha"): "トゥーンアルファ",
        ("*", "Toon UV"): "トゥーンUV",
        ("*", "Sphere Tex Fac"): "スフィアテクスチャ係数",
        ("*", "Sphere Tex"): "スフィアテクスチャ",
        ("*", "Sphere Alpha"): "スフィアアルファ",
        ("*", "Sphere UV"): "スフィアUV",
        ("*", "Sphere Mul/Add"): "スフィア 乗算/加算",
        ("*", "SubTex UV"): "サブテクスチャUV",
    },
    "zh_CN": {
        # Preferences
        ("*", "View3D > Tool Shelf > MMD Tools Panel"): "3D视图 > 侧栏 > MMD Tools面板",
        ("*", "Utility tools for MMD model editing. (powroupi's forked version)"): "用于MMD模型编辑的实用工具。(powroupi的分叉版本)",
        ("*", "Shared Toon Texture Folder"): "共用的卡通纹理文件夹",
        ("*", "Base Texture Folder"): "基线纹理文件夹",
        ("*", "Dictionary Folder"): "辞書文件夹",
        ("*", "Non-Collision Threshold"): "非碰撞阈值",

        # 3D Viewport > Sidebar > MMD > Operator Panel
        ("Operator", "Create Model"): "创建新的模型",
        ("Operator", "Create a MMD Model Root Object"): "创建一个MMD模型的根物体",
        ("*", "Name(Eng)"): "名称(英文)",

        ("Operator", "Convert Model"): "转换模型",
        ("Operator", "Convert to a MMD Model"): "转换为MMD模型",
        ("*", "Ambient Color Source"): "环境色源",
        ("*", "Edge Threshold"): "边缘阈值",
        ("*", "Minimum Edge Alpha"): "最小边缘Alpha",

        ("Operator", "Convert Materials For Cycles"): "转换材质给Cycles",
        ("*", "Convert to Principled BSDF"): "转换为原理化BSDF",
        ("*", "Clean Nodes"): "清理节点",
        ("Operator", "Separate By Materials"): "按材质分开",
        ("*", "Clean Shape Keys"): "清理形态键",
        ("Operator", "Join Meshes"): "合并网格",
        ("*", "Sort Shape Keys"): "排列形态键",
        ("Operator", "Attach Meshes to Model"): "将网格附上到模型",
        ("Operator", "Translation"): "翻译",
        ("Operator", "Translate a MMD Model"): "翻译一个MMD模型",
        ("*", "Dictionary"): "词典",
        ("*", "Modes"): "模式",
        ("*", "MMD Names"): "MMD名称",
        ("*", "Blender Names"): "Blender名称",
        ("*", "Use Morph Prefix"): "使用变形前缀",
        ("*", "Allow Fails"): "允许失败",

        ("*", "Bone Constraints:"): "骨骼约束:",
        ("*", "Physics:"): "物理:",
        ("Operator", "Build"): "建立",
        ("*", "Edge Preview:"): "边缘预览:",
        ("*", "Create"): "创建",
        ("*", "Clean"): "清空",
        ("*", "Model:"): "模型:",

        ("Operator", "Import"): "导入",
        ("*", "Types"): "类型",
        ("*", "Morphs"): "变形",
        ("*", "Clean Model"): "清空模型",
        ("*", "Fix IK Links"): "修复IK关联",
        ("*", "Apply Bone Fixed Axis"): "应用骨骼固定轴",
        ("*", "Rename Bones - L / R Suffix"): "将骨骼重命名 - L / R后缀",
        ("*", "Rename Bones - Use Underscore"): "将骨骼重命名 - 使用下划线",
        ("*", "Rename Bones To English"): "将骨骼重命名为英文",
        ("*", "Internal Dictionary"): "内部词典",
        ("*", "use MIP maps for UV textures"): "使用多级纹理进行UV纹理",
        ("*", "influence of .sph textures"): ".sph纹理的影响",
        ("*", "influence of .spa textures"): ".spa纹理的影响",
        ("*", "Log level"): "日志级别",
        ("*", "Create a log file"): "创建一个日志文件",
        ("*", "Copy textures"): "复制纹理",
        ("*", "Sort Materials"): "排列材质",
        ("*", "Disable SPH/SPA"): "禁用SPH/SPA",
        ("*", "Visible Meshes Only"): "只有可见的网格",
        ("*", "Sort Vertices"): "排列顶点",

        ("*", "Motion:"): "运动:",
        ("*", "Bone Mapper"): "骨骼映射器",
        ("*", "Renamed bones"): "重命名的骨骼",
        ("*", "Treat Current Pose as Rest Pose"): "把当前的姿态当作静置姿态",
        ("*", "Mirror Motion"): "镜像运动",
        ("*", "Update scene settings"): "更新场景设置",
        ("*", "Use Frame Range"): "使用帧范围",

        ("*", "Pose:"): "姿态:",
        ("*", "Current Pose"): "当前的姿态",
        ("*", "Active Pose"): "活动的姿态",
        ("*", "All Poses"): "全部姿态",

        # 3D Viewport > Sidebar > MMD > Display Panel
        ("*", "Display Panel"): "显示面板",
        ("Operator", "Bone"): "骨骼",
        ("Operator", "Morph"): "变形",
        ("Operator", "Add Display Item Frame"): "添加显示项目帧",
        ("Operator", "Remove Display Item Frame"): "移除显示项目帧",
        ("Operator", "Move Display Item Frame"): "移动显示项目帧",
        ("Operator", "Add Display Item"): "添加显示项目",
        ("Operator", "Remove Display Item"): "移除显示项目",
        ("Operator", "Move Display Item"): "移动显示项目",
        ("*", "Quick setup display items"): "快速设置显示项目",
        ("*", "Load Facial Items"): "载入面部项目",
        ("*", "Load Bone Groups"): "载入骨骼组",
        ("*", "Apply Bone Groups"): "应用骨骼组",
        ("Operator", "Move To Top"): "移至顶部",
        ("Operator", "Move To Bottom"): "移至底部",
        ("Operator", "Delete All"): "删除全部",

        # 3D Viewport > Sidebar > MMD > Morph Tools Panel
        ("*", "Morph Tools"): "变形工具",
        ("*", "Eye"): "眼",
        ("*", "Eye Brow"): "眼眉",
        ("*", "Mouth"): "嘴巴",
        ("Operator", "Add Morph"): "添加变形",
        ("Operator", "Remove Morph"): "移除变形",
        ("Operator", "Copy Morph"): "复制变形",
        ("Operator", "Move Morph"): "移动变形",
        ("Operator", "Add Morph Offset"): "添加变形偏移",
        ("Operator", "Remove Morph Offset"): "移除变形偏移",
        ("*", "Related Mesh"): "相关网格",
        ("Operator", "Create Work Material"): "创建工作材质",
        ("Operator", "Init Material Offset"): "初始化材质偏移",
        ("*", "Texture factor"): "纹理系数",
        ("*", "Sphere Texture factor"): "球体纹理系数",
        ("*", "Toon Texture factor"): "卡通纹理系数",

        # 3D Viewport > Sidebar > MMD > Rigid Bodies
        ("*", "Rigid Bodies"): "刚体",
        ("*", "Active Model"): "活动的模型",
        ("*", "All Models"): "全部模型",
        ("Operator", "Select Similar..."): "选择类似...",
        ("*", "Collision Group"): "碰撞组",
        ("*", "Collision Group Mask"): "碰撞组遮罩",
        ("*", "Rigid Type"): "刚类型",
        ("*", "Hide Others"): "隐藏其他",

        # 3D Viewport > Sidebar > MMD > Joints
        ("*", "Joints"): "关节",
        ("Operator", "Add Joint"): "添加关节",
        ("Operator", "Remove Joint"): "移除关节",

        # 3D Viewport > Sidebar > MMD > Material Sorter Panel
        ("*", "Material Sorter"): "材质顺序",
        ("*", "Select a mesh object"): "选择一个网格物体",
        ("*", "Use the arrows to sort"): "使用箭头来排序",
        ("Operator", "Move Material Up"): "移动材质",
        ("Operator", "Move Material Down"): "移动材质",

        # 3D Viewport > Sidebar > MMD > Meshes Sorter Panel
        ("*", "Meshes Sorter"): "网格顺序",
        ("*", "Select a MMD Model"): "选择一个MMD模型",
        ("Operator", "Move Object"): "移动物体",

        # 3D Viewport > Sidebar > MMD > Bone Order Panel
        ("*", "Bone Order"): "骨骼顺序",
        ("*", "After Dynamics"): "物理後",
        ("*", "Transform Order"): "変形階層",

        # 3D Viewport > Sidebar > Misc > MMD Display Panel
        ("*", "MMD Display"): "MMD显示",
        ("*", "Temporary Object"): "临时物体",
        ("*", "Rigid Body Name"): "刚体名称",
        ("*", "Joint"): "关节",
        ("*", "Joint Name"): "关节名称",
        ("*", "Toon Texture"): "卡通纹理",
        ("*", "Sphere Texture"): "球体纹理",
        ("*", "Property Drivers"): "属性驱动器",

        # 3D Viewport > Sidebar > Misc > MMD Shading Panel
        ("*", "MMD Shading"): "MMD着色",
        ("Operator", "Shadeless"): "无明暗",

        # 3D Viewport > Sidebar > Misc > MMD SDEF Driver Panel
        ("*", "MMD SDEF Driver"): "MMD SDEF驱动器",
        ("Operator", "Bind"): "绑定",
        ("Operator", "Unbind"): "解绑",
        ("*", "Bind SDEF Driver"): "绑定SDEF驱动器",
        ("*", "- Auto -"): "自动",
        ("*", "Bulk"): "散装",
        ("*", "Skip"): "略过",

        # Properties > Object Properties > MMD Lamp Tools
        ("*", "MMD Lamp Tools"): "MMD照明工具",
        ("Operator", "Convert to MMD Lamp"): "转换为MMD照明",
        ("*", "Light Source"): "光源",

        # Properties > Object Properties > MMD Camera Tools
        ("*", "MMD Camera Tools"): "MMD摄像机工具",
        ("Operator", "Convert to MMD Camera"): "转换为MMD摄像机",
        ("*", "Camera Source"): "摄像机源",

        # Properties > Object Properties > MMD Model Information Panel
        ("*", "MMD Model Information"): "MMD模型信息",
        ("*", "Name (English)"): "名称(英文)",
        ("*", "Comment (English)"): "注释(英文)",
        ("Operator", "Change MMD IK Loop Factor"): "改变MMD IK循环系数",
        ("*", "MMD IK Loop Factor"): "MMD IK循环系数",
        ("Operator", "Recalculate bone roll"): "重算骨骼扭转",
        ("*", "This operation will break existing f-curve/action."): "这一操作将破坏现有的函数曲线/动作。",
        ("*", "Click [OK] to run the operation."): "点击[确定]来运行操作。",

        # Properties > Object Properties > MMD Rigid Body
        ("*", "MMD Rigid Body"): "MMD刚体",
        ("*", "Physics + Bone"): "物理 + 骨骼",
        ("*", "Collision Group Mask:"): "碰撞组遮罩:",

        # Properties > Object Properties > MMD Joint
        ("*", "MMD Joint"): "MMD关节",
        ("*", "X-Axis:"): "X轴:",
        ("*", "Y-Axis:"): "Y轴:",
        ("*", "Z-Axis:"): "Z轴:",
        ("*", "Spring(Linear)"): "弹簧(线性)",
        ("*", "Spring(Angular)"): "弹簧(棱角)",

        # Properties > Material Properties > MMD Material Panel
        ("*", "MMD Material"): "MMD材质",
        ("*", "Color:"): "颜色:",
        ("*", "Shadow:"): "阴影:",
        ("*", "Double Sided"): "双面",
        ("*", "Ground Shadow"): "地面阴影",
        ("*", "Self Shadow Map"): "自身阴影贴图",
        ("*", "Self Shadow"): "自身阴影",
        ("*", "Toon Edge"): "卡通边缘",
        ("*", "Edge Color"): "边缘颜色",
        ("*", "Edge Weight"): "边缘权重",

        # Properties > Material Properties > MMD Texture Panel
        ("*", "MMD Texture"): "MMD纹理",
        ("*", "Texture:"): "纹理:",
        ("*", "Sphere Texture:"): "球体纹理:",
        ("*", "SubTexture"): "次纹理",
        ("*", "Use Shared Toon Texture"): "使用共用的卡通纹理",
        ("*", "Shared Toon Texture"): "共用的卡通纹理",

        # Properties > Bone Properties > MMD Bone Tools Panel
        ("*", "MMD Bone Tools"): "MMD骨骼工具",
        ("*", "Information:"): "信息:",
        ("*", "Controllable"): "可控制的",
        ("*", "Tip Bone"): "尖端骨骼",
        ("*", "Fixed Axis"): "轴制限",
        ("*", "Local Axes"): "局部轴",
        ("*", "Local X-Axis"): "局部X轴",
        ("*", "Local Z-Axis"): "局部Z轴",
        ("*", "Rotate +"): "旋转 +",
        ("*", "Move +"): "移动 +",

        # Shader Editor > Shader Nodes
        ("*", "Base Tex Fac"): "基线纹理系数",
        ("*", "Base Tex"): "基线纹理",
        ("*", "Base Alpha"): "基线Alpha",
        ("*", "Base UV"): "基线UV",
        ("*", "Toon Tex Fac"): "卡通纹理系数",
        ("*", "Toon Tex"): "卡通纹理",
        ("*", "Toon Alpha"): "卡通Alpha",
        ("*", "Toon UV"): "卡通UV",
        ("*", "Sphere Tex Fac"): "球体纹理系数",
        ("*", "Sphere Tex"): "球体纹理",
        ("*", "Sphere Alpha"): "球体Alpha",
        ("*", "Sphere UV"): "球体UV",
        ("*", "Sphere Mul/Add"): "球体 乘法/加法",
        ("*", "SubTex UV"): "次纹理UV",
    },
}
