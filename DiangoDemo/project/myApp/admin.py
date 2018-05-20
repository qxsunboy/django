from django.contrib import admin

# Register your models here.

from .models import Grades, Students


class StudentsInfo(admin.TabularInline):
    model = Students  # 表示这个对象为Students实例
    extra = 2  # 表示默认2条


# 自定义显示Grades
@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]  # 表示在创建Grades时同时添加一行或多行目标对象的实例
    # 列表页属性
    list_display = ['pk', 'gname', 'gdate', 'ggrilnum', 'gboynum', 'isDelete']  # 显示字段
    list_filter = ['gname']  # 过滤器，过滤字段
    search_fields = ['gname']  # 搜索器，搜索字段
    list_per_page = 5  # 每5条一页

    # 执行动作位置
    # actions_on_Top=False #显示在上
    # actions_on_bottom=True #显示在下,好像没卵用

    # 添加、修改页属性
    # fields=['ggrilnum','gboynum','gname','gdate','isDelete'] #修改添加页的显示顺序，不包括pk
    fieldsets = [
        ("num", {"fields": ['ggrilnum', 'gboynum']}),
        ("base", {"fields": ['gname', 'gdate', 'isDelete']}),
    ]  # 给属性分组，与上面的不能同时使用


#


# 注册，正式使用一般不用这种方式，而是用装饰器来完成注册,在自定义类上加上@admin.register(想要装饰的类名)
# admin.site.register(Grades,GradesAdmin)


# 自定义显示Students
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    # 布尔值显示方式修改
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"

    # 字段简短描述修改
    gender.short_description = "性别"

    # 列表页属性
    list_display = ['pk', 'sname', gender, 'sage', 'sconted', 'sgrade', 'isDelete']  # 显示字段
    list_filter = ['sname']  # 过滤器，过滤字段
    search_fields = ['sname']  # 搜索器，搜索字段
    list_per_page = 2  # 每5条一页

    # 添加、修改页属性
    # fields=['ggrilnum','gboynum','gname','gdate','isDelete'] #修改添加页的显示顺序，不包括pk
    fieldsets = [
        ("name", {"fields": ['sname', 'sgender']}),
        ("base", {"fields": ['sage', 'sconted', 'sgrade', 'isDelete']}),
    ]  # 给属性分组，与上面的不能同时使用

# 注册，正式使用一般不用这种方式，而是用装饰器来完成注册,在自定义类上加上@admin.register(想要装饰的类名)
# admin.site.register(Students,StudentsAdmin)
