from . import project1,project2

# 获得project1中的所有成员
member_p1= {name:getattr(project1,name)
            for name in project1.__all__ if hasattr(project1,name)}

member_p2= {name:getattr(project2,name)
            for name in project2.__all__ if hasattr(project2,name)}

# 更新当前模块的名称空间列表
cur_dict=globals()
cur_dict.update(member_p1)
cur_dict.update(member_p2)

__all__ = project1.__all__ + project2.__all__

