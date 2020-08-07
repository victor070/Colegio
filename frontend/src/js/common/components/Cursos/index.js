import { connect } from 'react-redux';
import { actions } from '../../../redux/modules/cursos/cursos';
import Cursos from './Cursos';


const ms2p = (state) => {
    return {
        ...state.curso,
        bandera: true,
    };
};

const md2p = { ...actions };

export default connect(ms2p, md2p)(Cursos);
