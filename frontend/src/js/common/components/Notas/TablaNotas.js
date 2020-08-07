import React, { Component } from 'react';


export default class TablaNotas extends Component {
    render() {
        return (
            <div className="py-4">
                <div className="row">
                    <div className="mb-4 col-12">
                        <div className="mb-4 card card-small">
                            <div className="border-bottom card-header"><h6 className="m-0">Idiomas</h6></div>
                            <div className="p-0 px-3 pt-3">
                                <table>
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Nombre</th>
                                            <th>Apellido</th>
                                            <th>Nota</th>

                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>1</td>
                                            <td>Victor</td>
                                            <td>Corado</td>
                                            <td>100</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
