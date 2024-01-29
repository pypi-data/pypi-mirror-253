import numpy as np


def test_wdm():
    # Create a WDM object
    from wdm_wavelet.wdm import WDM

    fake_strain = np.random.randn(4096)

    wdm = WDM(32, 64, 6, 10)
    m_L, nWWS, pWDM = wdm.t2w(fake_strain)

    assert len(pWDM) == 2
