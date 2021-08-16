# encoding=utf-8
import subprocess
import csv
import os


class version():
    def gitversion(self):
        browser = excute_cmd("dpkg -l |grep org.deepin.browser | awk '{if(\"org.deepin.browser\"==$2)print $3}'")

        dde_calendar = excute_cmd("dpkg -l |grep dde-calendar | awk '{if(\"dde-calendar\"==$2)print $3}'")

        dde_introduction = excute_cmd(
            "dpkg -l |grep dde-introduction | awk '{if(\"dde-introduction\"==$2)print $3}'")

        deepin_calculator = excute_cmd(
            "dpkg -l |grep deepin-calculator | awk '{if(\"deepin-calculator\"==$2)print $3}'")

        deepin_compressor = excute_cmd(
            "dpkg -l |grep deepin-compressor | awk '{if(\"deepin-compressor\"==$2)print $3}'")

        deepin_deb_installer = excute_cmd("dpkg -l |grep deepin-deb-installer | awk '{if("
                                          "\"deepin-deb-installer\"==$2)print $3}'")

        deepin_devicemanager = excute_cmd("dpkg -l |grep deepin-devicemanager | awk '{if("
                                          "\"deepin-devicemanager\"==$2)print $3}'")
        deepin_editor = excute_cmd("dpkg -l |grep deepin-editor | awk '{if(\"deepin-editor\"==$2)print $3}'")
        deepin_font_manager = excute_cmd(
            "dpkg -l |grep deepin-font-manager | awk '{if(\"deepin-font-manager\"==$2)print $3}'")
        deepin_log_viewer = excute_cmd(
            "dpkg -l |grep deepin-log-viewer | awk '{if(\"deepin-log-viewer\"==$2)print $3}'")

        deepin_mail = excute_cmd("dpkg -l | grep deepin-mail| awk '{if(\"deepin-mail\"==$2)print $3}'")

        deepin_manual = excute_cmd("dpkg -l |grep deepin-manual | awk '{if(\"deepin-manual\"==$2)print $3}'")

        deepin_reader = excute_cmd("dpkg -l |grep deepin-reader | awk '{if(\"deepin-reader\"==$2)print $3}'")
        deepin_system_monitor = excute_cmd("dpkg -l |grep deepin-system-monitor | awk '{if("
                                           "\"deepin-system-monitor\"==$2)print $3}'")

        deepin_terminal = excute_cmd("dpkg -l |grep deepin-terminal | awk '{if(\"deepin-terminal\"==$2)print $3}'")

        deepin_voice_note = excute_cmd(
            "dpkg -l |grep deepin-voice-note | awk '{if(\"deepin-voice-note\"==$2)print $3}'")

        uos_remote_assistance = excute_cmd(
            "dpkg -l |grep uos-remote-assistance| awk '{if(\"uos-remote-assistance\"==$2)print $3}'")

        uos_service_support = excute_cmd(
            "dpkg -l |grep uos-service-support | awk '{if(\"uos-service-support\"==$2)print $3}'")

        self.info_dict = {'BROWER': browser.strip(),
                          'DDE_CALENDAR': dde_calendar.strip(),
                          'dde_introduction': dde_introduction.strip(),
                          'deepin_calculator': deepin_calculator.strip(),
                          'deepin_compressor': deepin_compressor.strip(),
                          'deepin_deb_installer': deepin_deb_installer.strip(),
                          'deepin_devicemanager': deepin_devicemanager.strip(),
                          'deepin_editor': deepin_editor.strip(),
                          'deepin_font_manager': deepin_font_manager.strip(),
                          'deepin_log_viewer': deepin_log_viewer.strip(),
                          'deepin_mail': deepin_mail.strip(),
                          'deepin_manual': deepin_manual.strip(),
                          'deepin_reader': deepin_reader.strip(),
                          'deepin_system_monitor': deepin_system_monitor.strip(),
                          'deepin_terminal': deepin_terminal.strip(),
                          'deepin_voice_note': deepin_voice_note.strip(),
                          'uos_remote_assistance': uos_remote_assistance.strip(),
                          'uos_service_support': uos_service_support.strip(),
                          }
        return self.info_dict


def excute_cmd(cmd):
    """
    执行cmd命令,输出内容
    :param cmd:输入的命令
    :return:命令执行内容输出
    """
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, encoding='utf-8')
    out_msg = p.stdout.read()
    err_msg = p.stderr.read()
    if err_msg:
        return err_msg
    else:
        return out_msg


if __name__ == '__main__':
    versionName = version()
    pid = os.popen('echo $HOME')
    f = open(pid.read().strip() + '/Desktop/version.csv', 'w')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["程序名   ", "版本"])
    name = versionName.gitversion()
    for key, vaiule in name.items():
        # print(key + "  : " + str(vaiule))
        csv_writer.writerow([key, vaiule])
    f.close()
