import { connect } from 'react-redux';
import { actions } from '../../../redux/modules/notas/notas';
import Notas from './Notas';


const ms2p = (state) => {
    return {
        ...state.nota,
        bandera: true,
    };
};

const md2p = { ...actions };

export default connect(ms2p, md2p)(Notas);
