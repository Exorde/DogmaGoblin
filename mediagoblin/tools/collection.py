from mediagoblin import messages, mg_globals
from mediagoblin.db.models import (Collection,CollectionItem)
from mediagoblin.tools.response import redirect
from mediagoblin.tools.translate import pass_to_ugettext as _

def collection_tools(request, media, collection_form, new_media=False):

    if request.method != 'POST' or not collection_form.validate():
        # No POST submission, or invalid form
        if not form.validate():
            messages.add_message(request, messages.ERROR,
                _('Please check your entries and try again.'))

        return render_to_response(
            request,
            'mediagoblin/user_pages/media_collect.html',
            {'media': media,
             'collection_form': collection_form})

    # If we are here, method=POST and the form is valid, submit things.
    # If the user is adding a new collection, use that:
    if request.form['collection_title'] != '':
        # Make sure this user isn't duplicating an existing collection
        existing_collection = Collection.query.filter_by(
                                creator=request.user.id,
                                title=request.form['collection_title']).first()
        #If someone types an existing collection, use that collection
        if existing_collection:
            collection = existing_collection
        else:
            collection = Collection()
            collection.title = request.form['collection_title']
            collection.description = request.form.get('collection_description')
            collection.creator = request.user.id
            collection.generate_slug()
            collection.save()

    # Otherwise, use the collection selected from the drop-down
    elif request.form.get('collection') != '__None':
        collection = Collection.query.filter_by(
            id=request.form.get('collection')).first()
    elif new_media == False:
    # Make sure the user actually selected a collection
        messages.add_message(
            request, messages.ERROR,
            _('You have to select or add a collection'))
        return redirect(request, "mediagoblin.user_pages.media_home",
                    user=media.get_uploader.username,
                    media=media.id)
   #if there's no collection and it's a new media just do nothing
    else:
        return
       

    # Check whether media already exists in collection
    if CollectionItem.query.filter_by(
        media_entry=media.id,
        collection=collection.id).first():
        messages.add_message(request, messages.ERROR,
            _('"%s" already in collection "%s"'
                % (media.title, collection.title)))
    else: # Add item to collection
        collection_item = request.db.CollectionItem()
        collection_item.collection = collection.id
        collection_item.media_entry = media.id
        collection_item.author = request.user.id
        collection_item.note = request.form['note']
        collection_item.save()

        collection.items = collection.items + 1
        collection.save()

        media.collected = media.collected + 1
        media.save()

        messages.add_message(request, messages.SUCCESS,
                             _('"%s" added to collection "%s"'
                               % (media.title, collection.title)))

    return redirect(request, "mediagoblin.user_pages.media_home",
                    user=media.get_uploader.username,
                    media=media.id)
