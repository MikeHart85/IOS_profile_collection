from time import sleep
import numpy as np

def user_checkin():
    proposal_id = input('Enter your proposal number:  ')
    PI_name = input('Enter the last name of the PI:  ')
    endstation = input('Which endstation (APPES or IOXAS)?  ')
    cycle = input('Run cycle?  ')

    RE.md['PI'] = PI_name
    RE.md['proposal_id'] = proposal_id
    RE.md['endstation'] = endstation
    RE.md['cycle'] = cycle

def user_checkout():
    del RE.md['PI']
#    RE.md['group'] = ''
    del RE.md['proposal_id']
    del RE.md['endstation']
    del RE.md['cycle']

def save_xas_csv(first_id, last_id):
    for scanid in range(first_id,last_id+1,1):
        df = db[scanid].table()
        df['Norm'] = df['sclr_ch4']/df['sclr_ch3']
        #fn = 'csv_data/Scan_{scan_id}.csv'.format(db[scanid].start)
        df.to_csv('~/User_Data/Hunt/Prop_302802/Scan_%d.csv' % scanid, columns=['pgm_energy_readback', 'vortex_mca_rois_roi2_count', 'vortex_mca_rois_roi3_count', 'vortex_mca_rois_roi4_count', 'sclr_ch2', 'sclr_ch3', 'sclr_ch4', 'Norm'], index=False)

def save_xas_csv_short(first_id, last_id):
        for scanid in range(first_id,last_id+1,1):
                df = db.get_table(db[scanid])
                #fn = 'csv_data/Scan_{scan_id}.csv'.format(db[scanid].start)
                df.to_csv('~/User_Data/Quackenbush_XAS/Scan_%d.csv' % scanid, columns=['time', 'pgm_energy_readback', 'sclr_ch3', 'sclr_ch4', 'norm_ch4', 'ring_curr'])


def save_xas_csv_all(first_id, last_id):
        for scanid in range(first_id,last_id+1,1):
                df = db.get_table(db[scanid])
#                df['Norm'] = df['sclr_ch4']/df['sclr_ch3']
                #fn = 'csv_data/Scan_{scan_id}.csv'.format(db[scanid].start)
                df.to_csv('~/User_Data/Schroeder/Nov2017/Scan_%d.csv' % scanid, columns=['pgm_energy_readback', 'ioxas_x', 'sclr_ch2', 'sclr_ch3', 'sclr_ch4', 'vortex_mca_rois_roi3_count', 'vortex_mca_rois_roi4_count'], index=False)


def liveplot_photodiode():
     sclr.hints = {'fields': ['sclr_ch2']} 

def liveplot_xas():
     sclr.hints = {'fields': ['sclr_ch4']} 

def liveplot_aumesh():
     sclr.hints = {'fields': ['sclr_ch3']} 



def plot_norm_trans(scanid1,scanid2,normid,label):
        plt.figure(label)
        label = plt.gca()
        dfn = db.get_table(db[normid])
        for i in range (scanid1, scanid2+1):
                df1 = db.get_table(db[i])
                df1['Norm'] = -1*np.log(df1['sclr_ch4']/dfn['sclr_ch4'])
                df1.plot(x = 'pgm_energy_readback', y = 'Norm', label = str(i), ax=label)

def plot_norm_async_tey(scanid1,scanid2,normid,label):
        plt.figure(label)
        label = plt.gca()
        dfn = db.get_table(db[normid])
        for i in range (scanid1, scanid2+1):
                df1 = db.get_table(db[i])
                df1['Norm'] = df1['norm_ch4']/dfn['norm_ch4']
                df1.plot(x = 'pgm_energy_readback', y = 'Norm', label = str(i), ax=label)

def plot_sample_map(scanid1,scanid2,label):
        plt.figure(label)
        label = plt.gca()
        for i in range (scanid1, scanid2+1):
                df1 = db.get_table(db[i])
                df1.plot(x = 'ioxas_x', y = 'sclr_ch4', label = str(i), ax=label)

def plot_norm_async_pfy(scanid1,scanid2,normid,label):
        plt.figure(label)
        label = plt.gca()
        dfn = db.get_table(db[normid])
        for i in range (scanid1, scanid2+1):
                df1 = db.get_table(db[i])
                df1['Norm'] = df1['vortex_mca_rois_roi4_count']/dfn['sclr_ch2']
                df1.plot(x = 'pgm_energy_readback', y = 'Norm', label = str(i), ax=label)

def plot_norm_tey(scanid1,scanid2,label):
    plt.figure(label)
    label = plt.gca()
    for i in range (scanid1, scanid2+1):
        df1 = db.get_table(db[i])
        df1['Norm'] = df1['sclr_ch4']/df1['sclr_ch3']
        df1.plot(x = 'pgm_energy_readback', y = 'Norm', label = str(i), ax=label)

def plot_norm_pfy(scanid1,scanid2,label):
        plt.figure(label)
        label = plt.gca()
        for i in range (scanid1, scanid2+1):
                df1 = db.get_table(db[i])
                df1['Norm'] = df1['vortex_mca_rois_roi4_count']/df1['sclr_ch3']
                df1.plot(x = 'pgm_energy_readback', y = 'Norm', label = str(i), ax=label)

def plot_norm_pfy_ROI2(scanid1,scanid2,label):
        plt.figure(label)
        label = plt.gca()
        for i in range (scanid1, scanid2+1):
                df1 = db.get_table(db[i])
                df1['Norm'] = df1['vortex_mca_rois_roi2_count']/df1['sclr_ch3']
                df1.plot(x = 'pgm_energy_readback', y = 'Norm', label = str(i), ax=label)

def plot_norm_ipfy(scanid1,scanid2,label):
        plt.figure(label)
        label = plt.gca()
        for i in range (scanid1, scanid2+1):
                df1 = db.get_table(db[i])
                df1['Norm'] = 1/(df1['vortex_mca_rois_roi3_count']/df1['sclr_ch3'])
                df1.plot(x = 'pgm_energy_readback', y = 'Norm', label = str(i), ax=label)

def plot_raw_ipfy(scanid1,scanid2,label):
        plt.figure(label)
        label = plt.gca()
        for i in range (scanid1, scanid2+1):
                df1 = db.get_table(db[i])
                df1['IPFY'] = 1/(df1['vortex_mca_rois_roi3_count'])
                df1.plot(x = 'pgm_energy_readback', y = 'IPFY', label = str(i), ax=label)

def plot_raw_pfy(scanid1,scanid2,label):
        plt.figure(label)
        label = plt.gca()
        for i in range (scanid1, scanid2+1):
                df1 = db.get_table(db[i])
                df1.plot(x = 'pgm_energy_readback', y = 'vortex_mca_rois_roi4_count', label = str(i), ax=label)

def plot_raw_tey(scanid1,scanid2,label):
        plt.figure(label)
        label = plt.gca()
        for i in range (scanid1, scanid2+1):
                df1 = db.get_table(db[i])
                df1.plot(x = 'pgm_energy_readback', y = 'sclr_ch4', label = str(i), ax=label)


def XAS_scan(e_start, e_finish, velocity, deadband, inc_vortex = False ):
    if inc_vortex == True:
        for channel in ['mca.rois.roi2.count','mca.rois.roi3.count', 'mca.rois.roi4.count']:
            getattr(vortex, channel).kind = 'hinted'    
            dets = [sclr, vortex, norm_ch4, ring_curr]
    else:
         dets = [sclr, norm_ch4, ring_curr]

    for channel in ['channels.chan3','channels.chan4']:
        getattr(sclr, channel).kind = 'hinted'

    yield from bps.mov(pgm_energy, e_start)
    yield from E_ramp(dets, e_start, e_finish, velocity, deadband=deadband)
    
def epu_gap_scans():
    dets=[sclr, ring_curr]
    sclr.channels.chan2.kind = 'hinted'
    yield from bps.mov(diag3_y, 6)

   # for ene_val in range(250, 1251, 50):
    #    yield from bps.mov(pgm_energy, ene_val)
     #   yield from bps.sleep(10)
     #   yield from bp.rel_scan(dets, epu1.gap, -2, 2, 80)

    #for ene_val2 in range(1300, 1651, 50):
    #    yield from bps.mov(pgm_energy, ene_val2)
    #    yield from bps.sleep(10)
    #    yield from bp.rel_scan(dets, epu1.gap, -3, 3, 120)

    #caput('XF:23ID-ID{EPU:1}Val:Table-Sel',7)
    #yield from bps.sleep(10)
    #yield from bps.mov(pgm_energy, 750)

    #for ene_val3 in range(750, 1951, 50):
    #    yield from bps.mov(pgm_energy, ene_val3)
    #    yield from bps.sleep(10)
    #    yield from bp.rel_scan(dets, epu1.gap, -1.5, 1.5, 80)

    yield from bps.mov(epu1.phase, 24.6)
    yield from bps.sleep(10)
    caput('XF:23ID-ID{EPU:1}Val:Table-Sel',5)
    yield from bps.sleep(10)
    yield from bps.mov(pgm_energy, 450)
    
   
    for ene_val_v in range(450, 1251, 50):
        yield from bps.mov(pgm_energy, ene_val_v)
        yield from bps.sleep(10)
        yield from bp.rel_scan(dets, epu1.gap, -2, 2, 80)

    for ene_val_v2 in range(1300, 1651, 50):
        yield from bps.mov(pgm_energy, ene_val_v2)
        yield from bps.sleep(10)
        yield from bp.rel_scan(dets, epu1.gap, -3, 3, 120)

    caput('XF:23ID-ID{EPU:1}Val:Table-Sel',9)
    yield from bps.sleep(10)
    yield from bps.mov(pgm_energy, 1200)

    for ene_val_v3 in range(1200, 1951, 50):
        yield from bps.mov(pgm_energy, ene_val_v3)
        yield from bps.sleep(10)
        yield from bp.rel_scan(dets, epu1.gap, -1.5, 1.5, 80)
    
    yield from bps.mov(pgm_energy, 1200)
    yield from bps.mov(epu1.phase, 0)
    caput('XF:23ID-ID{EPU:1}Val:Table-Sel',6)
    yield from bps.mov(diag3_y, 46)    


def nexafs_pey(e_start, e_finish):
    # Set the detectors, because, YOLO
    dets = [sclr, norm_ch4, ring_curr]
    for channel in ['channels.chan3','channels.chan4']:
        getattr(sclr, channel).kind = 'hinted'   

    #turn off feedback before moving energy
    # caput('XF:23ID2-OP{FBck}Sts:FB-Sel',0)
    yield from bps.mov(mirror_feedback, 0)
    yield from bps.sleep(2)
    #to close downstream shutter
    # caput('XF:23ID2-PPS{PSh}Cmd:Cls-Cmd',1)
    yield from bps.mov(ds_shutter, 'Close')
    # sleep(2)
    print ('Moving to start energy...')
    #move energy to start position
    yield from bps.mov(pgm_energy, e_start)

    yield from bps.sleep(2)

    print ('Scan is starting...')

    #to open downstream shutter just when scan is started
    # caput('XF:23ID2-PPS{PSh}Cmd:Opn-Cmd',1)
    yield from bps.mov(ds_shutter, 'Open')    
    yield from bps.sleep(3)
    
    #turn on feedback
    # caput('XF:23ID2-OP{FBck}Sts:FB-Sel',1)
    yield from bps.mov(mirror_feedback, 1)    
    #caput('XF:23IDA-OP:2{Mir:1A-Ax:FPit}Mtr_POS_SP',50)
    #sleep(2)

    #to start the scan
    #RE(ascan(pgm_energy, e_start, e_finish, e_points), group='nexafs')
    yield from E_ramp(dets, e_start, e_finish, 0.05, deadband=6)

    # caput('XF:23ID2-OP{FBck}Sts:FB-Sel',0)
    yield from bps.mov(mirror_feedback, 0)
    yield from bps.sleep(2)
    #to close downstream shutter
    # caput('XF:23ID2-PPS{PSh}Cmd:Cls-Cmd',1)
    yield from bps.mov(ds_shutter, 'Close')
    # sleep(2)
    yield from bps.sleep(2)

    #to open downstream shutter just when scan is started
    # caput('XF:23ID2-PPS{PSh}Cmd:Opn-Cmd',1)
    yield from bps.mov(ds_shutter, 'Open')    
    yield from bps.sleep(3)
    
    #turn on feedback
    # caput('XF:23ID2-OP{FBck}Sts:FB-Sel',1)
    yield from bps.mov(mirror_feedback, 1)    

    #saving scan
#    save_q = input("The scan is finished. Do you want to save the data (as csv)? (yes/no) ")
#    if save_q in ["yes", "Y", "Yes", "y", "YES"]:
#        filename = input("Type file name here (no spaces, no special characters other than dash or underscore): ")
#        savedname = filename+'.csv'
#        df = db.get_table(db[-1])
#        df.to_csv('Documents/Yildiz/savedname')
#        print ('The scan has been saved as', savedname)
#    else:
#        print ('The scan has not been saved!')

def test():
    yield from abs_set(pgm_energy, 890, wait=True)
    yield from E_ramp(890, 895, 0.1, deadband=8)

def find_sample():
        # gs no longer supported
    #gs.TABLE_COLS.append('vortex_mca_rois_roi2_count')
    #gs.PLOT_Y = 'vortex_mca_rois_roi2_count'
#    mov(vortex.mca.rois.roi2.lo_chan, 1400)
#    mov(vortex.mca.rois.roi2.hi_chan, 2000)
    old_hints = save_hint_state(vortex)
    vortex.mca.rois.roi2.count.kind = 'hinted' 
    yield from bps.mov(pgm_energy, 1860)
    yield from bps.sleep(2)
    yield from bp.scan([sclr], ioxas_x, 245, 295, 250)
    yield from bps.sleep(2)
    restore_hint_state(vortex, old_hints)
    #gs.TABLE_COLS.remove('vortex_mca_rois_roi2_count')
    #gs.PLOT_Y = 'vortex_mca_rois_roi4_count'

def save_hint_state(dev):
    return {c: getattr(dev, c).kind for c in dev.read_attrs}

def restore_hint_state(dev, prev_state):
    for channel, state in prev_state.items():
        getattr(dev, channel).kind = state


