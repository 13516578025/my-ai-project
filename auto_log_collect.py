import xlrd
import paramiko
import time
import codecs
import os

# 定义ssh函数
def log_collect_bgp_peer():
    for row in range(1,rows):
        try:
            # 获取设备数据文件指定单元格内的值
            device_name = table.cell_value(rowx=row, colx=0)
            ip_address = table.cell_value(rowx=row, colx=1)
            port = int(table.cell_value(rowx=row, colx=3))
            username = table.cell_value(rowx=row, colx=4)
            password = table.cell_value(rowx=row, colx=5)
            # 执行ssh到设备操作
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ip_address,port=port,username=username,password=password)
            cli = ssh.invoke_shell()
            time.sleep(10)
            cli.send('screen-length 0 temporary\n')
            time.sleep(2)
            cli.send('dis bgp l2vpn-ad peer \n')
            time.sleep(10)
            dis_cu = cli.recv(999999).decode('utf-8', 'replace')
            file_name = file_path+date+'/'+device_name+'/dis_bgp_l2vpn-ad_peer.log'
            config_file = codecs.open(file_name,'w', 'utf-8')
            config_file.write(dis_cu)
            config_file.close()
            date2 = time.strftime("%Y-%m-%d, %H:%M:%S")
            print(date2+"  SSH登录"+device_name+" dis bgp l2vpn-ad peer 成功")
            logfile.write(date2+"  SSH登录"+device_name+" dis bgp l2vpn-ad peer 成功\n")
            ssh.close()
        except Exception as err:
            date2 = time.strftime("%Y-%m-%d, %H:%M:%S")
            print(date2+"  SSH登录"+device_name+"失败")
            logfile.write(date2+"  SSH登录"+device_name+"失败\n")
            ssh.close()

def log_collect_vsi():
    for row in range(1,rows):
        try:
            # 获取设备数据文件指定单元格内的值
            device_name = table.cell_value(rowx=row, colx=0)
            ip_address = table.cell_value(rowx=row, colx=1)
            port = int(table.cell_value(rowx=row, colx=3))
            username = table.cell_value(rowx=row, colx=4)
            password = table.cell_value(rowx=row, colx=5)
            # 执行ssh到设备操作
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ip_address,port=port,username=username,password=password)
            cli = ssh.invoke_shell()
            time.sleep(10)
            cli.send('screen-length 0 temporary\n')
            time.sleep(2)
            cli.send('dis vsi \n')
            time.sleep(10)
            dis_cu = cli.recv(999999).decode('utf-8', 'replace')
            file_name = file_path+date+'/'+device_name+'/dis_vsi.log'
            config_file = codecs.open(file_name,'w', 'utf-8')
            config_file.write(dis_cu)
            config_file.close()
            date2 = time.strftime("%Y-%m-%d, %H:%M:%S")
            print(date2+"  SSH登录"+device_name+" dis vsi 成功")
            logfile.write(date2+"  SSH登录"+device_name+" dis vsi 成功\n")
            ssh.close()
        except Exception as err:
            date2 = time.strftime("%Y-%m-%d, %H:%M:%S")
            print(date2+"  SSH登录"+device_name+"失败")
            logfile.write(date2+"  SSH登录"+device_name+"失败\n")
            ssh.close()


def log_collect_dis_inter_bri():
    for row in range(1,rows):
        try:
            # 获取设备数据文件指定单元格内的值
            device_name = table.cell_value(rowx=row, colx=0)
            ip_address = table.cell_value(rowx=row, colx=1)
            port = int(table.cell_value(rowx=row, colx=3))
            username = table.cell_value(rowx=row, colx=4)
            password = table.cell_value(rowx=row, colx=5)
            # 执行ssh到设备操作
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ip_address,port=port,username=username,password=password)
            cli = ssh.invoke_shell()
            time.sleep(10)
            cli.send('screen-length 0 temporary\n')
            time.sleep(2)
            cli.send('dis inter bri | exclude *down \n')
            time.sleep(10)
            dis_cu = cli.recv(999999).decode('utf-8', 'replace')
            file_name = file_path+date+'/'+device_name+'/dis_interface_bri.log'
            config_file = codecs.open(file_name,'w', 'utf-8')
            config_file.write(dis_cu)
            config_file.close()
            date2 = time.strftime("%Y-%m-%d, %H:%M:%S")
            print(date2+"  SSH登录"+device_name+" dis inter bri exclude *down 成功")
            logfile.write(date2+"  SSH登录"+device_name+" dis inter bri exclude *down 成功\n")
            ssh.close()
        except Exception as err:
            date2 = time.strftime("%Y-%m-%d, %H:%M:%S")
            print(date2+"  SSH登录"+device_name+"失败")
            logfile.write(date2+"  SSH登录"+device_name+"失败\n")
            ssh.close()


def log_collect_dis_inter():
    for row in range(1,rows):
        try:
        # 获取设备数据文件指定单元格内的值
            device_name = table.cell_value(rowx=row, colx=0)
            ip_address = table.cell_value(rowx=row, colx=1)
            port = int(table.cell_value(rowx=row, colx=3))
            username = table.cell_value(rowx=row, colx=4)
            password = table.cell_value(rowx=row, colx=5)
            # 执行ssh到设备操作
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ip_address,port=port,username=username,password=password)
            cli = ssh.invoke_shell()
            time.sleep(10)
            cli.send('screen-length 0 temporary\n')
            time.sleep(2)
            cli.send('dis interface \n')
            time.sleep(10)
            dis_cu = cli.recv(999999).decode('utf-8', 'replace')
            file_name = file_path+date+'/'+device_name+'/dis_interface.log'
            config_file = codecs.open(file_name,'w', 'utf-8')
            config_file.write(dis_cu)
            config_file.close()
            date2 = time.strftime("%Y-%m-%d, %H:%M:%S")
            print(date2+"  SSH登录"+device_name+" dis interface 成功")
            logfile.write(date2+"  SSH登录"+device_name+" dis interface 成功\n")
            ssh.close()
        except Exception as err:
            date2 = time.strftime("%Y-%m-%d, %H:%M:%S")
            print(date2+"  SSH登录"+device_name+"失败")
            logfile.write(date2+"  SSH登录"+device_name+"失败\n")
            ssh.close()


def log_collect_dis_eth_trunk():
    for row in range(1,rows):
        try:
            # 获取设备数据文件指定单元格内的值
            device_name = table.cell_value(rowx=row, colx=0)
            ip_address = table.cell_value(rowx=row, colx=1)
            port = int(table.cell_value(rowx=row, colx=3))
            username = table.cell_value(rowx=row, colx=4)
            password = table.cell_value(rowx=row, colx=5)
            # 执行ssh到设备操作
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ip_address,port=port,username=username,password=password)
            cli = ssh.invoke_shell()
            time.sleep(10)
            cli.send('screen-length 0 temporary\n')
            time.sleep(2)
            cli.send('dis eth-trunk \n')
            time.sleep(10)
            dis_cu = cli.recv(999999).decode('utf-8', 'replace')
            file_name = file_path+date+'/'+device_name+'/dis_eth-trunk.log'
            config_file = codecs.open(file_name,'w', 'utf-8')
            config_file.write(dis_cu)
            config_file.close()
            date2 = time.strftime("%Y-%m-%d, %H:%M:%S")
            print(date2+"  SSH登录"+device_name+" dis eth-trunk 成功")
            logfile.write(date2+"  SSH登录"+device_name+" dis eth-trunk 成功\n")
            ssh.close()
        except Exception as err:
            date2 = time.strftime("%Y-%m-%d, %H:%M:%S")
            print(date2+"  SSH登录"+device_name+"失败")
            logfile.write(date2+"  SSH登录"+device_name+"失败\n")
            ssh.close()


def log_collect_dis_inter_CRC():
    for row in range(1,rows):
        try:
            # 获取设备数据文件指定单元格内的值
            device_name = table.cell_value(rowx=row, colx=0)
            ip_address = table.cell_value(rowx=row, colx=1)
            port = int(table.cell_value(rowx=row, colx=3))
            username = table.cell_value(rowx=row, colx=4)
            password = table.cell_value(rowx=row, colx=5)
            # 执行ssh到设备操作
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ip_address,port=port,username=username,password=password)
            cli = ssh.invoke_shell()
            time.sleep(10)
            cli.send('screen-length 0 temporary\n')
            time.sleep(2)
            cli.send('dis inter | in CRC \n')
            time.sleep(10)
            dis_cu = cli.recv(999999).decode('utf-8', 'replace')
            file_name = file_path+date+'/'+device_name+'/dis_inter_in_CRC.log'
            config_file = codecs.open(file_name,'w', 'utf-8')
            config_file.write(dis_cu)
            config_file.close()
            date2 = time.strftime("%Y-%m-%d, %H:%M:%S")
            print(date2+"  SSH登录"+device_name+" dis inter | in CRC 成功")
            logfile.write(date2+"  SSH登录"+device_name+" dis inter | in CRC 成功\n")
            ssh.close()
        except Exception as err:
            date2 = time.strftime("%Y-%m-%d, %H:%M:%S")
            print(date2+"  SSH登录"+device_name+"失败")
            logfile.write(date2+"  SSH登录"+device_name+"失败\n")
            ssh.close()


def log_collect_dis_logbuffer():
    for row in range(1,rows):
        try:
        # 获取设备数据文件指定单元格内的值
            device_name = table.cell_value(rowx=row, colx=0)
            ip_address = table.cell_value(rowx=row, colx=1)
            port = int(table.cell_value(rowx=row, colx=3))
            username = table.cell_value(rowx=row, colx=4)
            password = table.cell_value(rowx=row, colx=5)
            # 执行ssh到设备操作
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ip_address,port=port,username=username,password=password)
            cli = ssh.invoke_shell()
            time.sleep(10)
            cli.send('screen-length 0 temporary\n')
            time.sleep(2)
            cli.send('dis logbuffer\n')
            time.sleep(10)
            cli.send('reset logbuffer \n')
            cli.send('y \n')
            dis_cu = cli.recv(999999).decode('utf-8', 'replace')
            file_name = file_path+date+'/'+device_name+'/dis_logbuffer.log'
            config_file = codecs.open(file_name,'w', 'utf-8')
            config_file.write(dis_cu)
            config_file.close()
            date2 = time.strftime("%Y-%m-%d, %H:%M:%S")
            print(date2+"  SSH登录"+device_name+" dis logbuffer 成功")
            logfile.write(date2+"  SSH登录"+device_name+" dis logbuffer 成功\n")
            ssh.close()
        except Exception as err:
            date2 = time.strftime("%Y-%m-%d, %H:%M:%S")
            print(date2+"  SSH登录"+device_name+"失败")
            logfile.write(date2+"  SSH登录"+device_name+"失败\n")
            ssh.close()


def log_collect_dis_power():
    for row in range(1,rows):
        try:
            # 获取设备数据文件指定单元格内的值
            device_name = table.cell_value(rowx=row, colx=0)
            ip_address = table.cell_value(rowx=row, colx=1)
            port = int(table.cell_value(rowx=row, colx=3))
            username = table.cell_value(rowx=row, colx=4)
            password = table.cell_value(rowx=row, colx=5)
            # 执行ssh到设备操作
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ip_address,port=port,username=username,password=password)
            cli = ssh.invoke_shell()
            time.sleep(10)
            cli.send('screen-length 0 temporary\n')
            time.sleep(2)
            cli.send('dis power \n')
            time.sleep(10)
            dis_cu = cli.recv(999999).decode('utf-8', 'replace')
            file_name = file_path+date+'/'+device_name+'/dis power.log'
            config_file = codecs.open(file_name,'w', 'utf-8')
            config_file.write(dis_cu)
            config_file.close()
            date2 = time.strftime("%Y-%m-%d, %H:%M:%S")
            print(date2+"  SSH登录"+device_name+" dis power 成功")
            logfile.write(date2+"  SSH登录"+device_name+" dis power 成功\n")
            ssh.close()
        except Exception as err:
            date2 = time.strftime("%Y-%m-%d, %H:%M:%S")
            print(date2+"  SSH登录"+device_name+"失败")
            logfile.write(date2+"  SSH登录"+device_name+"失败\n")
            ssh.close()



# 打开设备数据文件
device_database = xlrd.open_workbook('/var/log/huawei/log_collect/device_database2.xls')
# 通过Sheet名称获取指定工作表
table = device_database.sheet_by_name(sheet_name='Sheet1')
# 获取sheet中有效行数
rows = table.nrows
# 创建日期
date = time.strftime("%Y-%m-%d")
# 创建新配置备份目录
file_path = '/var/log/huawei/log_collect/'
mkdir = 'mkdir ' + file_path + date
os.system(mkdir)
# 创建操作日志文件
logfilepath = '/var/log/huawei/log_collect/'+date+'_auto_log_collect.log'
logfile = codecs.open(logfilepath,'w','utf-8')
# 创建设备LOG目录
for row in range(1, rows):
    device_name1 = table.cell_value(rowx=row, colx=0)
    mkdir2 = mkdir+'/'+device_name1
    os.system(mkdir2)
# 打印操作前配置成功
date2 = time.strftime("%Y-%m-%d, %H:%M:%S")
print(date2+"  操作前全局配置成功")
logfile.write(date2+"  操作前全局配置成功\n")



if __name__=='__main__':
    log_collect_bgp_peer()
    log_collect_vsi()
    log_collect_dis_inter_bri()
    log_collect_dis_inter()
    log_collect_dis_eth_trunk()
    log_collect_dis_inter_CRC()
    log_collect_dis_logbuffer()
    log_collect_dis_power()
